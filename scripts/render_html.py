"""통합 보고서 데이터를 읽기 쉬운 단일 HTML 문서로 렌더링한다.

사용법:
  python3 scripts/render_html.py <template.json> <merge-dir> <out.html> \
      --title "..." --lens "..." --date YYYY-MM-DD [--groups <groups.json>]

입력:
  <merge-dir>/rows.json      merge_report.mjs prepare 가 만든 대상별 데이터
  <merge-dir>/sections.json  작성 에이전트가 쓴 [{key, markdown}]
  groups.json (선택)          {"order": [...], "groups": {앱이름: 유형}, "badges": {앱이름: 배지}}

필요: pip install markdown
"""
import argparse
import html
import json
import re
from pathlib import Path

import markdown

ap = argparse.ArgumentParser()
ap.add_argument("template")
ap.add_argument("merge_dir")
ap.add_argument("out")
ap.add_argument("--title", default="리서치 보고서")
ap.add_argument("--lens", default="")
ap.add_argument("--date", default="")
ap.add_argument("--groups")
a = ap.parse_args()

T = json.loads(Path(a.template).read_text(encoding="utf-8"))
data = json.loads((Path(a.merge_dir) / "rows.json").read_text(encoding="utf-8"))
sections = {s["key"]: s["markdown"] for s in json.loads((Path(a.merge_dir) / "sections.json").read_text(encoding="utf-8"))}
G = json.loads(Path(a.groups).read_text(encoding="utf-8")) if a.groups else {"order": [], "groups": {}, "badges": {}}
rows = data["rows"]
unverified = data["unverified"]
label = {f["key"]: f["label"] for f in T["fields"]}
esc = html.escape


def group_of(name):
    return G["groups"].get(name, "기타")


order = G.get("order") or []
for r in rows:
    g = group_of(r["name"])
    if g not in order:
        order.append(g)


def slug(name):
    return "app-" + str(rows.index(next(r for r in rows if r["name"] == name)))


# ───────── markdown → html (에이전트가 쓴 Markdown을 python-markdown에 맞게 보정) ─────────
LIST_RE = re.compile(r"^(\s*)([-*]|\d+\.)\s")


def normalize_md(md):
    out = []
    prev = ""
    for line in md.splitlines():
        m = LIST_RE.match(line)
        if m:
            indent = len(m.group(1))
            line = " " * ((indent + 1) // 2 * 4) + line.lstrip()
            if prev.strip() and not LIST_RE.match(prev):
                out.append("")
        elif line.startswith("|") and prev.strip() and not prev.startswith("|"):
            out.append("")
        out.append(line)
        prev = line
    return "\n".join(out)


TAGS = [
    (r"\[근거\]", '<span class="tag tag-ev">근거</span>'),
    (r"\(추론\)", '<span class="tag tag-inf">추론</span>'),
    (r"\(미확인\)", '<span class="tag tag-unk">미확인</span>'),
    (r"\(대\)", '<span class="tag tag-scale" title="대형·성숙 앱">대</span>'),
    (r"\(중\)", '<span class="tag tag-scale" title="중간 규모">중</span>'),
    (r"\(소\)", '<span class="tag tag-scale tag-small" title="소형·신생 앱">소</span>'),
]


def md(text):
    h = markdown.markdown(normalize_md(text), extensions=["tables", "sane_lists"])
    for pat, rep in TAGS:
        h = re.sub(pat, rep, h)
    h = h.replace("<table>", '<div class="table-wrap"><table>').replace("</table>", "</table></div>")
    return h


MARK = {
    "confirmed": ('<span class="mk mk-ok" title="독립 검증에서 확인">✓</span>'),
    "corrected": ('<span class="mk mk-fix" title="검증에서 수정됨">✎</span>'),
    "unverifiable": ('<span class="mk mk-unk" title="검증 불가">?</span>'),
}


def mark(f):
    return MARK.get((f or {}).get("status"), "")


def short(r, key):
    f = r["fields"].get(key)
    if not f:
        return '<span class="muted">–</span>'
    return esc(f.get("short") or f.get("value") or "") + mark(f)


# ───────── sections ─────────
parts = []
toc = []


def section(sid, title, body, lead=""):
    toc.append((sid, title))
    parts.append(f'<section id="{sid}"><h2>{esc(title)}</h2>{lead}{body}</section>')


section("summary", "요약", f'<div class="callout">{md(sections.get("summary", ""))}</div>')

if "implications" in sections:
    section("flow", "제안: 사진 선택 → 레이아웃 흐름", md(sections["implications"]),
            '<p class="lead">조사한 앱 사례를 근거로 한 이어북 사진 선택 화면 설계안이다. '
            '<span class="tag tag-ev">근거</span> 앱 사례 확인 · <span class="tag tag-inf">추론</span> 데이터에서 유추 · '
            '<span class="tag tag-scale">대</span>/<span class="tag tag-scale tag-small">소</span> 근거 앱 규모</p>')

# app cards by group
cards = []
for g in order:
    items = [r for r in rows if group_of(r["name"]) == g]
    if not items:
        continue
    cs = []
    for r in items:
        badge = G.get("badges", {}).get(r["name"])
        cs.append(
            f'<a class="card" href="#{slug(r["name"])}" data-group="{esc(g)}">'
            f'<div class="card-head"><strong>{esc(r["name"])}</strong>'
            + (f'<span class="badge">{esc(badge)}</span>' if badge else "")
            + f'</div><div class="card-meta">{short(r, "scale")}</div>'
            f'<div class="card-body">{short(r, "lens_features")}</div></a>'
        )
    cards.append(f'<h3>{esc(g)} <span class="count">{len(items)}</span></h3><div class="cards">{"".join(cs)}</div>')
section("apps", "앱 한눈에 보기", "".join(cards),
        '<p class="lead">카드를 누르면 앱별 상세로 이동한다. ✓ 독립 검증 확인 · ✎ 검증에서 수정 · ? 검증 불가</p>')

if "patterns" in sections:
    section("patterns", "관점별 기능 패턴", md(sections["patterns"]))

# comparison table
cols = ["developer", "scale", "lens_features", "ai", "pricing"]
chips = '<div class="chips"><button class="chip on" data-f="*">전체</button>' + "".join(
    f'<button class="chip" data-f="{esc(g)}">{esc(g)}</button>' for g in order
) + "</div>"
trs = []
for g in order:
    for r in rows:
        if group_of(r["name"]) != g:
            continue
        trs.append(
            f'<tr data-group="{esc(g)}"><th scope="row"><a href="#{slug(r["name"])}">{esc(r["name"])}</a>'
            f'<div class="sub">{esc(g)}</div></th>' + "".join(f"<td>{short(r, k)}</td>" for k in cols) + "</tr>"
        )
table = (
    chips + '<div class="table-wrap"><table class="cmp"><thead><tr><th>앱</th>'
    + "".join(f"<th>{esc(label.get(k, k))}</th>" for k in cols)
    + "</tr></thead><tbody>" + "".join(trs) + "</tbody></table></div>"
)
section("compare", "비교표", table, '<p class="lead">유형별로 걸러 볼 수 있다. 값은 요약이며 출처는 앱별 상세에 있다.</p>')

# details
det = []
for g in order:
    for r in rows:
        if group_of(r["name"]) != g:
            continue
        lis = []
        for f in T["fields"]:
            v = r["fields"].get(f["key"])
            if not v:
                continue
            srcs = " ".join(
                f'<a class="src" href="{esc(u)}" target="_blank" rel="noopener">{i + 1}</a>'
                for i, u in enumerate(v.get("sources") or [])
            )
            note = f'<div class="note">{esc(v["note"])}</div>' if v.get("note") else ""
            lis.append(f'<dt>{esc(f["label"])}{mark(v)}</dt><dd>{esc(v.get("value", ""))}{note}'
                       + (f'<div class="srcs">출처 {srcs}</div>' if srcs else "") + "</dd>")
        if r.get("extra"):
            lis.append(f'<dt>기타</dt><dd>{esc(r["extra"])}</dd>')
        badge = G.get("badges", {}).get(r["name"])
        det.append(
            f'<details id="{slug(r["name"])}"><summary><span class="dname">{esc(r["name"])}</span>'
            f'<span class="sub">{esc(g)}{" · " + esc(badge) if badge else ""}</span></summary>'
            f'<dl>{"".join(lis)}</dl></details>'
        )
section("details", "앱별 상세", "".join(det),
        '<p class="lead">항목을 펼치면 조사 값과 출처 링크를 볼 수 있다. <button class="linkbtn" id="expand">모두 펼치기</button></p>')

# unverified grouped by app
by_app = {}
for u in unverified:
    name = next((r["name"] for r in rows if u.startswith(r["name"])), "기타")
    by_app.setdefault(name, []).append(u[len(name):].lstrip(" :/").strip() if name != "기타" else u)
ublocks = "".join(
    f'<details><summary><span class="dname">{esc(n)}</span><span class="sub">{len(items)}개</span></summary>'
    f'<ul>{"".join(f"<li>{esc(i)}</li>" for i in items)}</ul></details>'
    for n, items in by_app.items()
)
section("gaps", f"확인하지 못한 것 ({len(unverified)}개)", ublocks,
        '<p class="lead">공개 자료로 확인하지 못한 항목이다. 실제 앱을 설치해 화면을 확인하면 대부분 풀린다.</p>')

nav = "".join(f'<a href="#{sid}">{esc(t)}</a>' for sid, t in toc)
n_groups = ", ".join(f"{g} {sum(1 for r in rows if group_of(r['name']) == g)}" for g in order)

HTML = f"""<!doctype html>
<html lang="ko">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(a.title)}</title>
<style>
:root {{
  --bg: #fbfaf8; --panel: #ffffff; --ink: #1f2328; --muted: #6a6f76; --line: #e6e3de;
  --accent: #2f5bd3; --accent-soft: #eaf0ff; --ev: #1f7a4d; --ev-soft: #e5f4ec;
  --inf: #8a5a00; --inf-soft: #fff3d9; --unk: #a1352b; --unk-soft: #fde9e6; --chip: #f1efeb;
}}
@media (prefers-color-scheme: dark) {{
  :root:not([data-theme="light"]) {{
    --bg: #15171a; --panel: #1d2024; --ink: #e8e6e3; --muted: #9aa0a6; --line: #2e3238;
    --accent: #8aa8ff; --accent-soft: #1f2a44; --ev: #6fd3a0; --ev-soft: #173326;
    --inf: #f0c46a; --inf-soft: #3a2e14; --unk: #ff9a8f; --unk-soft: #3d1f1c; --chip: #262a30;
  }}
}}
:root[data-theme="dark"] {{
  --bg: #15171a; --panel: #1d2024; --ink: #e8e6e3; --muted: #9aa0a6; --line: #2e3238;
  --accent: #8aa8ff; --accent-soft: #1f2a44; --ev: #6fd3a0; --ev-soft: #173326;
  --inf: #f0c46a; --inf-soft: #3a2e14; --unk: #ff9a8f; --unk-soft: #3d1f1c; --chip: #262a30;
}}
* {{ box-sizing: border-box; }}
html {{ scroll-behavior: smooth; scroll-padding-top: 16px; }}
body {{ margin: 0; background: var(--bg); color: var(--ink);
  font: 16px/1.7 -apple-system, BlinkMacSystemFont, "Apple SD Gothic Neo", "Noto Sans KR", "Malgun Gothic", "Segoe UI", sans-serif;
  word-break: keep-all; overflow-wrap: anywhere; }}
a {{ color: var(--accent); text-decoration: none; }}
a:hover {{ text-decoration: underline; }}
.layout {{ display: grid; grid-template-columns: 220px minmax(0, 1fr); gap: 40px; max-width: 1180px; margin: 0 auto; padding: 32px 24px 80px; }}
main {{ min-width: 0; }}
nav.toc {{ position: sticky; top: 24px; align-self: start; display: flex; flex-direction: column; gap: 2px; font-size: 14px; }}
nav.toc .tt {{ font-weight: 700; color: var(--muted); font-size: 12px; letter-spacing: .04em; margin-bottom: 6px; }}
nav.toc a {{ color: var(--muted); padding: 6px 10px; border-radius: 8px; }}
nav.toc a:hover, nav.toc a.on {{ background: var(--accent-soft); color: var(--accent); text-decoration: none; }}
header.hero {{ margin-bottom: 28px; }}
header.hero h1 {{ font-size: 30px; line-height: 1.3; margin: 0 0 12px; letter-spacing: -0.01em; }}
.meta {{ display: flex; flex-wrap: wrap; gap: 8px; margin-top: 12px; }}
.meta span {{ background: var(--chip); border-radius: 999px; padding: 4px 12px; font-size: 13px; color: var(--muted); }}
.lens {{ color: var(--muted); margin: 0; }}
section {{ background: var(--panel); border: 1px solid var(--line); border-radius: 16px; padding: 28px 32px; margin-bottom: 24px; }}
section h2 {{ font-size: 22px; margin: 0 0 8px; }}
section h3 {{ font-size: 17px; margin: 28px 0 10px; }}
section h3:first-of-type {{ margin-top: 16px; }}
.lead {{ color: var(--muted); font-size: 14px; margin: 0 0 16px; }}
.callout {{ background: var(--accent-soft); border-radius: 12px; padding: 4px 20px; }}
.callout li {{ margin: 10px 0; }}
ul, ol {{ padding-left: 22px; }}
li {{ margin: 4px 0; }}
.tag {{ display: inline-block; font-size: 12px; font-weight: 600; line-height: 1.5; padding: 0 7px; border-radius: 6px; vertical-align: 1px; }}
.tag-ev {{ background: var(--ev-soft); color: var(--ev); }}
.tag-inf {{ background: var(--inf-soft); color: var(--inf); }}
.tag-unk {{ background: var(--unk-soft); color: var(--unk); }}
.tag-scale {{ background: var(--chip); color: var(--muted); padding: 0 5px; }}
.tag-small {{ border: 1px dashed var(--muted); }}
.mk {{ display: inline-block; margin-left: 4px; font-size: 12px; font-weight: 700; }}
.mk-ok {{ color: var(--ev); }} .mk-fix {{ color: var(--inf); }} .mk-unk {{ color: var(--unk); }}
.cards {{ display: grid; grid-template-columns: repeat(auto-fill, minmax(250px, 1fr)); gap: 12px; }}
.card {{ display: block; border: 1px solid var(--line); border-radius: 12px; padding: 14px 16px; color: var(--ink); background: var(--bg); transition: border-color .15s, transform .15s; }}
.card:hover {{ border-color: var(--accent); text-decoration: none; transform: translateY(-1px); }}
.card-head {{ display: flex; gap: 8px; align-items: baseline; justify-content: space-between; margin-bottom: 4px; line-height: 1.4; }}
.card-meta {{ font-size: 12.5px; color: var(--muted); margin-bottom: 8px; }}
.card-body {{ font-size: 14px; line-height: 1.55; }}
.badge {{ flex: none; font-size: 11px; background: var(--inf-soft); color: var(--inf); border-radius: 6px; padding: 1px 6px; }}
.count {{ font-size: 13px; color: var(--muted); font-weight: 500; }}
.chips {{ display: flex; flex-wrap: wrap; gap: 6px; margin-bottom: 14px; }}
.chip {{ border: 1px solid var(--line); background: var(--panel); color: var(--ink); border-radius: 999px; padding: 5px 12px; font: inherit; font-size: 13px; cursor: pointer; }}
.chip.on {{ background: var(--accent); border-color: var(--accent); color: #fff; }}
.table-wrap {{ overflow-x: auto; border: 1px solid var(--line); border-radius: 12px; margin: 12px 0; }}
table {{ border-collapse: collapse; width: 100%; font-size: 14px; line-height: 1.5; }}
th, td {{ text-align: left; vertical-align: top; padding: 10px 12px; border-bottom: 1px solid var(--line); }}
thead th {{ background: var(--chip); font-size: 13px; position: sticky; top: 0; }}
tbody tr:last-child th, tbody tr:last-child td {{ border-bottom: 0; }}
table.cmp th[scope=row] {{ min-width: 170px; }}
table.cmp td {{ min-width: 150px; }}
.sub {{ font-size: 12px; color: var(--muted); font-weight: 400; }}
.muted {{ color: var(--muted); }}
details {{ border: 1px solid var(--line); border-radius: 12px; margin: 8px 0; background: var(--bg); }}
details[open] {{ background: var(--panel); }}
summary {{ cursor: pointer; padding: 12px 16px; display: flex; gap: 10px; align-items: baseline; flex-wrap: wrap; list-style: none; }}
summary::-webkit-details-marker {{ display: none; }}
summary::before {{ content: "▸"; color: var(--muted); transition: transform .15s; }}
details[open] > summary::before {{ transform: rotate(90deg); }}
.dname {{ font-weight: 600; }}
details dl {{ margin: 0; padding: 4px 20px 16px; display: grid; grid-template-columns: 140px minmax(0, 1fr); gap: 10px 16px; }}
details dt {{ font-weight: 600; font-size: 14px; color: var(--muted); }}
details dd {{ margin: 0; font-size: 14.5px; }}
details ul {{ margin: 0; padding: 0 20px 14px 40px; font-size: 14px; }}
.note {{ font-size: 13px; color: var(--muted); margin-top: 4px; }}
.srcs {{ font-size: 12.5px; color: var(--muted); margin-top: 4px; }}
.src {{ display: inline-block; min-width: 20px; text-align: center; background: var(--chip); border-radius: 5px; margin-right: 3px; }}
.linkbtn {{ background: none; border: 0; color: var(--accent); font: inherit; cursor: pointer; padding: 0; }}
.theme {{ position: fixed; right: 16px; bottom: 16px; border: 1px solid var(--line); background: var(--panel); color: var(--ink); border-radius: 999px; padding: 8px 14px; font: inherit; font-size: 13px; cursor: pointer; }}
footer {{ color: var(--muted); font-size: 13px; text-align: center; margin-top: 32px; }}
@media (max-width: 860px) {{
  .layout {{ grid-template-columns: minmax(0, 1fr); padding: 20px 16px 72px; gap: 0; }}
  nav.toc {{ position: static; flex-direction: row; overflow-x: auto; margin-bottom: 16px; white-space: nowrap; }}
  nav.toc .tt {{ display: none; }}
  section {{ padding: 20px 18px; border-radius: 14px; }}
  header.hero h1 {{ font-size: 24px; }}
  details dl {{ grid-template-columns: 1fr; gap: 2px; }}
  details dd {{ margin-bottom: 10px; }}
}}
@media print {{
  nav.toc, .theme, .chips, .linkbtn {{ display: none; }}
  .layout {{ display: block; }}
  section {{ break-inside: auto; border: 0; padding: 0; }}
}}
</style>
</head>
<body>
<div class="layout">
<nav class="toc" aria-label="목차"><div class="tt">목차</div>{nav}</nav>
<main>
<header class="hero">
<h1>{esc(a.title)}</h1>
<p class="lens"><strong>관점</strong> · {esc(a.lens)}</p>
<div class="meta"><span>기준일 {esc(a.date)}</span><span>대상 {len(rows)}개</span><span>{esc(n_groups)}</span><span>미확인 {len(unverified)}개</span></div>
</header>
{"".join(parts)}
<footer>research-harness로 생성 · 값 대부분은 스토어 설명·공식 자료 기준이며 실제 앱 화면으로 검증하지 않았다.</footer>
</main>
</div>
<button class="theme" id="theme" aria-label="테마 전환">◐ 테마</button>
<script>
(function () {{
  var root = document.documentElement;
  try {{ var t = localStorage.getItem("rh-theme"); if (t) root.setAttribute("data-theme", t); }} catch (e) {{}}
  document.getElementById("theme").onclick = function () {{
    var dark = root.getAttribute("data-theme") === "dark" ||
      (!root.getAttribute("data-theme") && matchMedia("(prefers-color-scheme: dark)").matches);
    var next = dark ? "light" : "dark";
    root.setAttribute("data-theme", next);
    try {{ localStorage.setItem("rh-theme", next); }} catch (e) {{}}
  }};
  document.querySelectorAll(".chip").forEach(function (c) {{
    c.onclick = function () {{
      document.querySelectorAll(".chip").forEach(function (x) {{ x.classList.remove("on"); }});
      c.classList.add("on");
      var f = c.getAttribute("data-f");
      document.querySelectorAll("table.cmp tbody tr").forEach(function (tr) {{
        tr.style.display = (f === "*" || tr.getAttribute("data-group") === f) ? "" : "none";
      }});
    }};
  }});
  var exp = document.getElementById("expand");
  if (exp) exp.onclick = function () {{
    var ds = document.querySelectorAll("#details details");
    var open = !ds[0].open;
    ds.forEach(function (d) {{ d.open = open; }});
    exp.textContent = open ? "모두 접기" : "모두 펼치기";
  }};
  function openTarget() {{
    var el = location.hash && document.querySelector(location.hash);
    if (el && el.tagName === "DETAILS") el.open = true;
  }}
  window.addEventListener("hashchange", openTarget); openTarget();
  var links = document.querySelectorAll("nav.toc a");
  var obs = new IntersectionObserver(function (es) {{
    es.forEach(function (e) {{
      if (e.isIntersecting) links.forEach(function (l) {{ l.classList.toggle("on", l.getAttribute("href") === "#" + e.target.id); }});
    }});
  }}, {{ rootMargin: "-30% 0px -60% 0px" }});
  document.querySelectorAll("main > section").forEach(function (s) {{ obs.observe(s); }});
}})();
</script>
</body>
</html>
"""
Path(a.out).write_text(HTML, encoding="utf-8")
print(f"저장: {a.out} ({len(HTML):,}자)")
