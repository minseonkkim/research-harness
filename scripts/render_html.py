"""통합 보고서를 훑어보기 쉬운 단일 HTML 문서로 렌더링한다.

사용법:
  python3 scripts/render_html.py <template.json> <merge-dir> <out.html> \
      --title "..." --lens "..." --date YYYY-MM-DD

<merge-dir> 안에서 읽는 파일:
  rows.json      merge_report.mjs prepare 가 만든 대상별 원본 데이터 (부록의 원문·출처)
  sections.json  작성 에이전트의 패턴 분석 원문 (부록)
  profiles.json  앱별 요약 카드 데이터 (필수, SKILL.md 참고)
  brief.json     요약·선택 흐름 (필수, SKILL.md 참고)
  groups.json    {"order": [...], "groups": {이름: 유형}, "badges": {이름: 배지}} (선택)
  links.json     {이름: {"play": 패키지, "ios": 앱ID, "galaxy": 패키지, "web": URL}} (선택)

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
a = ap.parse_args()

D = Path(a.merge_dir)


def load(name, default=None):
    p = D / name
    return json.loads(p.read_text(encoding="utf-8")) if p.exists() else default


T = json.loads(Path(a.template).read_text(encoding="utf-8"))
data = load("rows.json")
rows, unverified = data["rows"], data["unverified"]
sections = {s["key"]: s["markdown"] for s in load("sections.json", [])}
profiles = {p["name"]: p for p in load("profiles.json")}
brief = load("brief.json")
G = load("groups.json", {"order": [], "groups": {}, "badges": {}})
LINKS = load("links.json", {})
esc = html.escape
label = {f["key"]: f["label"] for f in T["fields"]}

order = list(G.get("order") or [])
group_of = lambda n: G["groups"].get(n, "기타")
for r in rows:
    if group_of(r["name"]) not in order:
        order.append(group_of(r["name"]))
idx = {r["name"]: i for i, r in enumerate(rows)}
aid = lambda n: f"app-{idx[n]}"
ordered = [r for g in order for r in rows if group_of(r["name"]) == g]


def short_name(n):
    return re.split(r"\s+[-–:(]|:\s", n)[0].strip()


# ───────── markdown (부록용) ─────────
LIST_RE = re.compile(r"^(\s*)([-*]|\d+\.)\s")


def normalize_md(md):
    out, prev = [], ""
    for line in md.splitlines():
        m = LIST_RE.match(line)
        if m:
            line = " " * ((len(m.group(1)) + 1) // 2 * 4) + line.lstrip()
            if prev.strip() and not LIST_RE.match(prev):
                out.append("")
        elif line.startswith("|") and prev.strip() and not prev.startswith("|"):
            out.append("")
        out.append(line)
        prev = line
    return "\n".join(out)


def md(text):
    h = markdown.markdown(normalize_md(text), extensions=["tables", "sane_lists"])
    for pat, rep in [(r"\[근거\]", '<span class="tag ev">근거</span>'), (r"\(추론\)", '<span class="tag inf">추론</span>'),
                     (r"\(미확인\)", '<span class="tag unk">미확인</span>')]:
        h = re.sub(pat, rep, h)
    return h.replace("<table>", '<div class="tw"><table>').replace("</table>", "</table></div>")


def inline(s):
    s = esc(s)
    return s.replace("(미확인)", '<span class="tag unk">미확인</span>').replace("(추론)", '<span class="tag inf">추론</span>')


# ───────── store buttons ─────────
def store_buttons(name):
    L = LINKS.get(name, {})
    b = []
    if L.get("play"):
        b.append(("Google Play", f"https://play.google.com/store/apps/details?id={L['play']}", "play"))
    if L.get("galaxy"):
        b.append(("Galaxy Store", f"https://galaxystore.samsung.com/detail/{L['galaxy']}", "play"))
    if L.get("ios"):
        b.append(("App Store", f"https://apps.apple.com/kr/app/id{L['ios']}", "ios"))
    if L.get("web"):
        b.append(("웹사이트", L["web"], "web"))
    if not b:
        return '<div class="stores"><span class="muted">설치 링크 없음</span></div>'
    return '<div class="stores">' + "".join(
        f'<a class="store {k}" href="{esc(u)}" target="_blank" rel="noopener">{esc(t)} ↗</a>' for t, u, k in b) + "</div>"


# ───────── matrix ─────────
MCOLS = [("child_filter", "아이 자동 필터"), ("similar_group", "유사 사진 묶기"), ("best_cut", "베스트컷 추천"),
         ("junk_filter", "불필요 사진 제외"), ("auto_suggest", "기간별 자동 제안"), ("review_ui", "자동 선택 후 검토"),
         ("progress", "월 분할·이어하기"), ("swipe", "스와이프 판정")]
SYM = {"yes": '<span class="m y" title="있음"></span>', "partial": '<span class="m p" title="일부"></span>',
       "no": '<span class="m n" title="없음"></span>', "unknown": '<span class="m u" title="미확인">?</span>'}

parts, nav = [], []


def section(sid, title, body, lead=""):
    nav.append((sid, title))
    parts.append(f'<section id="{sid}"><h2>{esc(title)}</h2>{lead}{body}</section>')


# 1. 요약
section("summary", "핵심 요약",
        '<ol class="summary">' + "".join(f"<li>{inline(s)}</li>" for s in brief["summary"]) + "</ol>")

# 2. 기능 비교
chips = '<div class="chips"><button class="chip on" data-f="*">전체 ' + str(len(rows)) + "</button>" + "".join(
    f'<button class="chip" data-f="{esc(g)}">{esc(g)} {sum(1 for r in rows if group_of(r["name"]) == g)}</button>'
    for g in order) + "</div>"
trs = []
for g in order:
    trs.append(f'<tr class="grp" data-group="{esc(g)}"><th colspan="{len(MCOLS) + 1}">{esc(g)}</th></tr>')
    for r in [r for r in rows if group_of(r["name"]) == g]:
        mx = profiles.get(r["name"], {}).get("matrix", {})
        trs.append(f'<tr data-group="{esc(g)}"><th scope="row"><a href="#{aid(r["name"])}">{esc(short_name(r["name"]))}</a></th>'
                   + "".join(f"<td>{SYM.get(mx.get(k, 'unknown'), SYM['unknown'])}</td>" for k, _ in MCOLS) + "</tr>")
matrix = (chips + '<div class="tw"><table class="matrix"><thead><tr><th>앱</th>'
          + "".join(f"<th>{esc(t)}</th>" for _, t in MCOLS) + "</tr></thead><tbody>" + "".join(trs) + "</tbody></table></div>"
          + '<p class="legend"><span class="m y"></span> 있음 <span class="m p"></span> 일부 <span class="m n"></span> 없음 <span class="m u">?</span> 미확인 · 앱 이름을 누르면 상세 카드로 이동</p>')
section("matrix", "기능 비교", matrix, '<p class="lead">사진 선택에 관련된 기능만 골라 표시했다.</p>')

# 3. 앱 목록
cards = []
for g in order:
    items = [r for r in rows if group_of(r["name"]) == g]
    cs = []
    for r in items:
        p = profiles.get(r["name"], {})
        badge = G.get("badges", {}).get(r["name"])
        info = "".join(f"<div><dt>{k}</dt><dd>{inline(p.get(f, '') or '–')}</dd></div>"
                       for k, f in [("개발사", "developer"), ("규모", "scale"), ("가격", "price"), ("AI 처리", "ai")])
        feats = "".join(f"<li>{inline(x)}</li>" for x in p.get("selection_features", []))
        take = "".join(f"<li>{inline(x)}</li>" for x in p.get("takeaways", []))
        cons = "".join(f"<li>{inline(x)}</li>" for x in p.get("cons", []))
        raw = []
        for f in T["fields"]:
            v = r["fields"].get(f["key"])
            if not v:
                continue
            srcs = " ".join(f'<a href="{esc(u)}" target="_blank" rel="noopener">[{i + 1}]</a>'
                            for i, u in enumerate((v.get("sources") or [])[:6]))
            raw.append(f"<dt>{esc(f['label'])}</dt><dd>{esc(v.get('value', ''))} <span class='srcs'>{srcs}</span></dd>")
        cs.append(
            f'<article class="app" id="{aid(r["name"])}">'
            f'<header><div class="tags"><span class="type">{esc(g)}</span>'
            + (f'<span class="badge">{esc(badge)}</span>' if badge else "")
            + f'</div><h3>{esc(r["name"])}</h3><p class="one">{inline(p.get("one_liner", ""))}</p></header>'
            + store_buttons(r["name"])
            + f'<dl class="info">{info}</dl>'
            + (f'<h4>사진 선택 관련 기능</h4><ul class="feats">{feats}</ul>' if feats else "")
            + (f'<div class="take"><h4>이어북에 참고할 점</h4><ul>{take}</ul></div>' if take else "")
            + (f'<h4>아쉬운 점</h4><ul class="cons">{cons}</ul>' if cons else "")
            + (f'<p class="caution">⚠ {inline(p["caution"])}</p>' if p.get("caution") else "")
            + f'<details class="raw"><summary>조사 원문과 출처</summary><dl>{"".join(raw)}</dl></details>'
            "</article>")
    cards.append(f'<div class="grp-block" data-group="{esc(g)}"><h3 class="gh">{esc(g)} <span class="count">{len(items)}</span></h3>'
                 f'<div class="apps">{"".join(cs)}</div></div>')
section("apps", "앱별 정리", "".join(cards), '<p class="lead">설치 링크 · 기본 정보 · 사진 선택 관련 기능 · 참고할 점 순서. 원문과 출처는 카드 아래 펼치기.</p>')

# 4. 선택 흐름
steps = []
for s in brief["flow"]:
    refs = "".join(f'<span class="ref">{esc(x)}</span>' for x in s.get("refs", []))
    steps.append(
        f'<li class="step"><div class="num">{esc(str(s["step"]))}</div><div class="sb">'
        f'<h3>{esc(s["title"])}' + (' <span class="tag inf">추론 위주</span>' if s.get("inferred") else "") + "</h3>"
        f'<p class="what">{inline(s["what"])}</p><ul>' + "".join(f"<li>{inline(x)}</li>" for x in s.get("how", [])) + "</ul>"
        + (f'<div class="refs">근거 앱 {refs}</div>' if refs else "") + "</div></li>")
yr = brief.get("year_round")
yr_html = (f'<div class="yr"><h3>{esc(yr["title"])}</h3><ul>' + "".join(f"<li>{inline(x)}</li>" for x in yr.get("how", []))
           + "</ul>" + (f'<div class="refs">근거 앱 ' + "".join(f'<span class="ref">{esc(x)}</span>' for x in yr.get("refs", [])) + "</div>")
           + "</div>") if yr else ""
cau = ('<div class="cautions"><h3>주의할 점</h3><ul>' + "".join(f"<li>{inline(x)}</li>" for x in brief.get("cautions", []))
       + "</ul></div>") if brief.get("cautions") else ""
section("flow", "제안: 사진 선택 흐름", f'<ol class="steps">{"".join(steps)}</ol>{yr_html}{cau}',
        '<p class="lead">조사한 앱 사례로 만든 이어북 사진 선택 → 레이아웃 설계안.</p>')

# 5. 부록
by_app = {}
for u in unverified:
    n = next((r["name"] for r in rows if u.startswith(r["name"])), "기타")
    by_app.setdefault(n, []).append(u[len(n):].lstrip(" :/").strip() if n != "기타" else u)
gaps = "".join(f'<details><summary>{esc(short_name(n))} <span class="count">{len(v)}</span></summary><ul>'
               + "".join(f"<li>{esc(x)}</li>" for x in v) + "</ul></details>" for n, v in by_app.items())
appx = ((f'<details class="big"><summary>기능 패턴 분석 원문</summary><div class="prose">{md(sections["patterns"])}</div></details>'
         if sections.get("patterns") else "")
        + (f'<details class="big"><summary>기획 시사점 원문</summary><div class="prose">{md(sections["implications"])}</div></details>'
           if sections.get("implications") else "")
        + f'<details class="big"><summary>확인하지 못한 것 ({len(unverified)}개)</summary><div class="prose">{gaps}</div></details>')
section("appendix", "부록", appx, '<p class="lead">원래의 긴 분석 글과 미확인 항목.</p>')

navhtml = "".join(f'<a href="#{i}">{esc(t)}</a>' for i, t in nav)
meta = (f"<span>기준일 {esc(a.date)}</span><span>앱 {len(rows)}개</span>"
        + "".join(f"<span>{esc(g)} {sum(1 for r in rows if group_of(r['name']) == g)}</span>" for g in order))

CSS = """
:root{--bg:#f7f6f3;--panel:#fff;--ink:#1d2127;--muted:#6b7078;--line:#e7e4df;--soft:#f1efeb;--accent:#2f5bd3;--asoft:#eaf0ff;
--ev:#1d7a4c;--evs:#e3f4ea;--inf:#8a5a00;--infs:#fff2d6;--unk:#a3362b;--unks:#fde8e5;--play:#0b8a4a;--ios:#1d6fe0}
@media (prefers-color-scheme:dark){:root:not([data-theme=light]){--bg:#141619;--panel:#1c1f23;--ink:#e9e7e4;--muted:#9ca2a9;--line:#2d3137;
--soft:#24282d;--accent:#8fadff;--asoft:#1e2942;--ev:#72d6a3;--evs:#163225;--inf:#f1c56b;--infs:#382c13;--unk:#ff9b90;--unks:#3b1e1b;--play:#5fd69a;--ios:#8fb8ff}}
:root[data-theme=dark]{--bg:#141619;--panel:#1c1f23;--ink:#e9e7e4;--muted:#9ca2a9;--line:#2d3137;--soft:#24282d;--accent:#8fadff;--asoft:#1e2942;
--ev:#72d6a3;--evs:#163225;--inf:#f1c56b;--infs:#382c13;--unk:#ff9b90;--unks:#3b1e1b;--play:#5fd69a;--ios:#8fb8ff}
*{box-sizing:border-box}html{scroll-behavior:smooth;scroll-padding-top:72px}
body{margin:0;background:var(--bg);color:var(--ink);font:16px/1.65 -apple-system,BlinkMacSystemFont,"Apple SD Gothic Neo","Noto Sans KR","Malgun Gothic","Segoe UI",sans-serif;word-break:keep-all;overflow-wrap:anywhere}
a{color:var(--accent);text-decoration:none}a:hover{text-decoration:underline}
.top{position:sticky;top:0;z-index:5;background:color-mix(in srgb,var(--bg) 88%,transparent);backdrop-filter:blur(8px);border-bottom:1px solid var(--line)}
.top nav{max-width:1120px;margin:0 auto;padding:10px 24px;display:flex;gap:4px;overflow-x:auto;white-space:nowrap}
.top a{color:var(--muted);padding:6px 12px;border-radius:999px;font-size:14px}.top a.on,.top a:hover{background:var(--asoft);color:var(--accent);text-decoration:none}
main{max-width:1120px;margin:0 auto;padding:32px 24px 80px}
.hero h1{font-size:30px;line-height:1.3;margin:0 0 10px;letter-spacing:-.01em}.hero p{color:var(--muted);margin:0}
.meta{display:flex;flex-wrap:wrap;gap:6px;margin:14px 0 28px}.meta span{background:var(--soft);border-radius:999px;padding:3px 11px;font-size:13px;color:var(--muted)}
section{margin-bottom:44px}section>h2{font-size:23px;margin:0 0 6px}.lead{color:var(--muted);font-size:14px;margin:0 0 16px}
.summary{background:var(--panel);border:1px solid var(--line);border-radius:16px;padding:20px 24px 20px 48px;margin:0}
.summary li{margin:8px 0;padding-left:4px}.summary li::marker{color:var(--accent);font-weight:700}
.tag{display:inline-block;font-size:11.5px;font-weight:600;padding:0 6px;border-radius:5px;line-height:1.6;vertical-align:1px}
.tag.ev{background:var(--evs);color:var(--ev)}.tag.inf{background:var(--infs);color:var(--inf)}.tag.unk{background:var(--unks);color:var(--unk)}
.chips{display:flex;flex-wrap:wrap;gap:6px;margin-bottom:12px}
.chip{border:1px solid var(--line);background:var(--panel);color:var(--ink);border-radius:999px;padding:5px 12px;font:inherit;font-size:13px;cursor:pointer}
.chip.on{background:var(--accent);border-color:var(--accent);color:#fff}
.tw{overflow-x:auto;background:var(--panel);border:1px solid var(--line);border-radius:14px}
table{border-collapse:collapse;width:100%;font-size:14px}th,td{padding:9px 12px;border-bottom:1px solid var(--line);text-align:left;vertical-align:top}
.matrix td{text-align:center;vertical-align:middle;min-width:76px}.matrix thead th{font-size:12.5px;color:var(--muted);text-align:center;background:var(--soft);line-height:1.35}
.matrix thead th:first-child{text-align:left}.matrix th[scope=row]{white-space:nowrap;font-weight:600}
.matrix tr.grp th{background:var(--soft);font-size:12.5px;color:var(--muted);padding:6px 12px}
.m{display:inline-block;width:14px;height:14px;border-radius:50%;vertical-align:-2px}.m.y{background:var(--ev)}
.m.p{border:2px solid var(--inf);background:linear-gradient(90deg,var(--inf) 50%,transparent 50%)}
.m.n{width:6px;height:6px;background:var(--line);vertical-align:1px}.m.u{width:auto;height:auto;color:var(--muted);font-size:13px;font-weight:700}
.legend{font-size:13px;color:var(--muted);margin:10px 2px}.legend .m{margin:0 3px 0 10px}.legend .m:first-child{margin-left:0}
.gh{font-size:17px;margin:28px 0 12px}.count{font-size:13px;color:var(--muted);font-weight:500}
.apps{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:16px}
.app{background:var(--panel);border:1px solid var(--line);border-radius:16px;padding:20px 22px;display:flex;flex-direction:column}
.app:target{border-color:var(--accent);box-shadow:0 0 0 3px var(--asoft)}
.app header h3{font-size:18px;margin:6px 0 2px;line-height:1.35}.one{color:var(--muted);font-size:14px;margin:0}
.tags{display:flex;gap:6px;flex-wrap:wrap}.type,.badge{font-size:11.5px;border-radius:6px;padding:1px 7px}.type{background:var(--soft);color:var(--muted)}.badge{background:var(--infs);color:var(--inf)}
.stores{display:flex;flex-wrap:wrap;gap:6px;margin:14px 0 12px}
.store{font-size:13px;font-weight:600;border:1px solid var(--line);border-radius:8px;padding:5px 11px;color:var(--ink);background:var(--bg)}
.store.play{color:var(--play)}.store.ios{color:var(--ios)}.store:hover{border-color:currentColor;text-decoration:none}
.info{display:grid;grid-template-columns:1fr 1fr;gap:8px 14px;margin:0 0 6px;padding:12px 14px;background:var(--bg);border-radius:10px}
.info dt{font-size:12px;color:var(--muted)}.info dd{margin:0;font-size:14px;line-height:1.45}
.app h4{font-size:13.5px;margin:14px 0 4px;color:var(--muted)}
.app ul{margin:0;padding-left:18px;font-size:14.5px}.app li{margin:3px 0}
.take{background:var(--asoft);border-radius:10px;padding:2px 14px 10px;margin-top:14px}.take h4{color:var(--accent)}
.cons li::marker{color:var(--unk)}
.caution{font-size:12.5px;color:var(--inf);margin:12px 0 0}
.raw{margin-top:auto;padding-top:14px}.raw summary{font-size:13px;color:var(--muted);cursor:pointer}
.raw dl{font-size:13px;margin:8px 0 0}.raw dt{font-weight:600;margin-top:8px}.raw dd{margin:2px 0 0;color:var(--muted)}.srcs a{font-size:12px}
.steps{list-style:none;padding:0;margin:0;position:relative}
.steps::before{content:"";position:absolute;left:19px;top:8px;bottom:8px;width:2px;background:var(--line)}
.step{display:flex;gap:16px;margin-bottom:14px;position:relative}
.num{flex:none;width:40px;height:40px;border-radius:50%;background:var(--accent);color:#fff;font-weight:700;display:grid;place-items:center;z-index:1}
.sb{flex:1;background:var(--panel);border:1px solid var(--line);border-radius:14px;padding:14px 18px}
.sb h3{font-size:16.5px;margin:0 0 2px}.what{margin:0 0 6px;color:var(--muted);font-size:14.5px}.sb ul{margin:0;padding-left:18px;font-size:14.5px}
.refs{margin-top:8px;font-size:12px;color:var(--muted)}.ref{display:inline-block;background:var(--soft);border-radius:5px;padding:0 6px;margin:2px 0 0 4px;color:var(--ink)}
.yr,.cautions{background:var(--panel);border:1px solid var(--line);border-radius:14px;padding:14px 18px;margin-top:14px}.yr h3,.cautions h3{font-size:16px;margin:0 0 6px}
.cautions{background:var(--infs);border-color:transparent}.yr ul,.cautions ul{margin:0;padding-left:18px;font-size:14.5px}
details.big{background:var(--panel);border:1px solid var(--line);border-radius:14px;margin:10px 0}
details.big>summary{padding:14px 18px;cursor:pointer;font-weight:600}.prose{padding:0 22px 16px;font-size:14.5px}
.prose details summary{cursor:pointer;padding:4px 0}.prose details ul{margin:2px 0 8px}
.muted{color:var(--muted);font-size:13px}
.theme{position:fixed;right:16px;bottom:16px;border:1px solid var(--line);background:var(--panel);color:var(--ink);border-radius:999px;padding:8px 14px;font:inherit;font-size:13px;cursor:pointer}
footer{color:var(--muted);font-size:13px;text-align:center}
@media (max-width:860px){main{padding:20px 16px 72px}.top nav{padding:8px 12px}.hero h1{font-size:24px}.apps{grid-template-columns:minmax(0,1fr)}
.app{padding:16px}.info{grid-template-columns:1fr 1fr}.summary{padding:14px 16px 14px 36px}}
@media print{.top,.theme,.chips{display:none}.app{break-inside:avoid}details{display:block}}
"""

JS = """
(function(){var r=document.documentElement;try{var t=localStorage.getItem("rh-theme");if(t)r.setAttribute("data-theme",t)}catch(e){}
document.getElementById("theme").onclick=function(){var d=r.getAttribute("data-theme")==="dark"||(!r.getAttribute("data-theme")&&matchMedia("(prefers-color-scheme: dark)").matches);
var n=d?"light":"dark";r.setAttribute("data-theme",n);try{localStorage.setItem("rh-theme",n)}catch(e){}};
document.querySelectorAll(".chip").forEach(function(c){c.onclick=function(){document.querySelectorAll(".chip").forEach(function(x){x.classList.remove("on")});c.classList.add("on");
var f=c.getAttribute("data-f");document.querySelectorAll(".matrix tbody tr").forEach(function(tr){tr.style.display=(f==="*"||tr.getAttribute("data-group")===f)?"":"none"})}});
var links=document.querySelectorAll(".top a");var o=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting)links.forEach(function(l){l.classList.toggle("on",l.getAttribute("href")==="#"+e.target.id)})})},{rootMargin:"-80px 0px -75% 0px"});
document.querySelectorAll("main>section").forEach(function(s){o.observe(s)});})();
"""

HTML = f"""<!doctype html>
<html lang="ko"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(a.title)}</title><style>{CSS}</style></head>
<body>
<div class="top"><nav aria-label="목차">{navhtml}</nav></div>
<main>
<header class="hero"><h1>{esc(a.title)}</h1><p>{esc(a.lens)}</p><div class="meta">{meta}</div></header>
{"".join(parts)}
<footer>research-harness로 생성 · 대부분 스토어 설명·공식 자료 기준이며 실제 앱 화면으로 검증하지 않았다.</footer>
</main>
<button class="theme" id="theme" aria-label="테마 전환">◐ 테마</button>
<script>{JS}</script>
</body></html>
"""
Path(a.out).write_text(HTML, encoding="utf-8")
print(f"저장: {a.out} ({len(HTML):,}자)")
