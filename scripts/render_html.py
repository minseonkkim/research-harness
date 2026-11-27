"""통합 보고서를 단일 HTML 문서로 렌더링한다: 1) 앱별 설명 카드 2) 관점에 맞는 기능 추천순.

사용법:
  python3 scripts/render_html.py <template.json> <merge-dir> <out.html> \
      --title "..." --lens "..." --date YYYY-MM-DD

<merge-dir> 안에서 읽는 파일:
  rows.json      merge_report.mjs prepare 가 만든 대상별 원본 데이터 (부록의 원문·출처)
  sections.json  작성 에이전트의 패턴 분석 원문 (부록)
  profiles.json  앱별 요약 카드 데이터 (필수, SKILL.md 참고)
  features.json  이어북 추천 기능 순위 (필수, SKILL.md 참고)
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
ap.add_argument("--tech", help="기능별 기술 구현 데이터(tech.json). 주면 3번 섹션을 추가한다")
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
FEATURES = load("features.json", [])
MEDIA = load("media.json", {})      # {앱이름: {icon, shots[]}} — scripts/fetch_store_media.py
GUIDE = load("guide.json", None)    # 처음 읽는 사람을 위한 안내·용어집
# 앱 카드의 '조사 원문'에 보여 줄 필드. 관점과 무관한 가격·규모·개인정보·일반 불만은 뺀다.
RAW_FIELDS = {"lens_features", "ai"}
TECH = json.loads(Path(a.tech).read_text(encoding="utf-8")) if a.tech else None
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


parts, nav = [], []


def section(sid, title, body, lead=""):
    nav.append((sid, title))
    parts.append(f'<section id="{sid}"><h2>{esc(title)}</h2>{lead}{body}</section>')


# 3. 앱 목록
cards = []
for g in order:
    items = [r for r in rows if group_of(r["name"]) == g]
    cs = []
    for r in items:
        p = profiles.get(r["name"], {})
        badge = G.get("badges", {}).get(r["name"])
        # 관점(사진 정리)과 무관한 개발사·규모·가격은 보여 주지 않는다. 분석 처리 방식만 남긴다.
        info = "".join(f"<div><dt>{k}</dt><dd>{inline(p.get(f, '') or '–')}</dd></div>"
                       for k, f in [("정리 분석 처리 방식", "ai")])
        feats = "".join(f"<li>{inline(x)}</li>" for x in p.get("selection_features", []))
        fl = p.get("flow") or {}
        ACT = {"자동": "a-auto", "사용자": "a-user", "자동+확인": "a-mix"}
        flow_html = ""
        if fl.get("steps"):
            flow_html = (
                '<div class="flow"><h4>사진 정리 흐름</h4>'
                + (f'<p class="ftitle">{inline(fl.get("title", ""))}</p>' if fl.get("title") else "")
                + '<ol class="fsteps">' + "".join(
                    f'<li><div class="fs-head"><span class="fs-name">{esc(s.get("name", ""))}</span>'
                    f'<span class="actor {ACT.get(s.get("actor"), "a-mix")}">{esc(s.get("actor", ""))}</span></div>'
                    f'<p>{inline(s.get("detail", ""))}</p></li>' for s in fl["steps"]) + "</ol>"
                + (f'<p class="fbasis">근거 · {inline(fl["basis"])}</p>' if fl.get("basis") else "")
                + "</div>")
        take = "".join(f"<li>{inline(x)}</li>" for x in p.get("takeaways", []))
        cons = "".join(f"<li>{inline(x)}</li>" for x in p.get("cons", []))
        raw = []
        for f in T["fields"]:
            if f["key"] not in RAW_FIELDS:
                continue
            v = r["fields"].get(f["key"])
            if not v:
                continue
            srcs = " ".join(f'<a href="{esc(u)}" target="_blank" rel="noopener">[{i + 1}]</a>'
                            for i, u in enumerate((v.get("sources") or [])[:6]))
            raw.append(f"<dt>{esc(f['label'])}</dt><dd>{esc(v.get('value', ''))} <span class='srcs'>{srcs}</span></dd>")
        md_ = MEDIA.get(r["name"], {})
        icon = (f'<img class="appicon" src="{esc(md_["icon"])}=w96" alt="" loading="lazy" referrerpolicy="no-referrer">'
                if md_.get("icon") else '<div class="appicon ph">' + esc(short_name(r["name"])[:1]) + "</div>")
        shots = ("".join(f'<img src="{esc(u)}=h480" alt="{esc(short_name(r["name"]))} 스크린샷 {i + 1}" loading="lazy" referrerpolicy="no-referrer">'
                         for i, u in enumerate(md_.get("shots", [])))
                 if md_.get("shots") else "")
        cs.append(
            f'<article class="app" id="{aid(r["name"])}">'
            f'<header class="apphead">{icon}<div><div class="tags"><span class="type">{esc(g)}</span>'
            + (f'<span class="badge">{esc(badge)}</span>' if badge else "")
            + f'</div><h3>{esc(r["name"])}</h3><p class="one">{inline(p.get("one_liner", ""))}</p></div></header>'
            + (f'<p class="plain">{inline(p["plain"])}</p>' if p.get("plain") else "")
            + (f'<div class="shots" aria-label="스토어 스크린샷">{shots}</div>' if shots else "")
            + store_buttons(r["name"])
            + f'<dl class="info">{info}</dl>'
            + flow_html
            + (f'<h4>주요 정리 기능</h4><ul class="feats chiplist">{feats}</ul>' if feats else "")
            + (f'<div class="take"><h4>이어북에 참고할 점</h4><ul>{take}</ul></div>' if take else "")
            + (f'<h4>정리 기능의 한계</h4><ul class="cons">{cons}</ul>' if cons else "")
            + (f'<p class="caution">⚠ {inline(p["caution"])}</p>' if p.get("caution") else "")
            + f'<details class="raw"><summary>정리 기능 조사 원문과 출처</summary><dl>{"".join(raw)}</dl></details>'
            "</article>")
    cards.append(f'<div class="grp-block" data-group="{esc(g)}"><h3 class="gh">{esc(g)} <span class="count">{len(items)}</span></h3>'
                 f'<div class="apps">{"".join(cs)}</div></div>')
section("apps", "1. 앱별 설명", "".join(cards),
        '<p class="lead">앨범 정리 기능만 다룬다. 설치 링크 · 사진 정리 흐름(단계별) · 주요 기능 · 이어북에 참고할 점 · 한계 순서. '
        '단계 표시: <span class="actor a-auto">자동</span> 앱이 처리 · <span class="actor a-mix">자동+확인</span> 앱이 제안하고 사용자가 확인 · '
        '<span class="actor a-user">사용자</span> 사용자가 직접. 원문과 출처는 카드 아래 펼치기.</p>')

# 2. 이어북 추천 기능 (추천순)
TIER = {"필수": "t1", "추천": "t2", "고려": "t3"}
fs = []
for f in FEATURES:
    apps = "".join(
        f'<li><a href="#{aid(x["name"])}">{esc(short_name(x["name"]))}</a> <span class="an">{inline(x.get("note", ""))}</span></li>'
        if x["name"] in idx else f'<li>{esc(x["name"])} <span class="an">{inline(x.get("note", ""))}</span></li>'
        for x in f.get("apps", []))
    fs.append(
        f'<article class="feat" id="feat-{esc(str(f["rank"]))}"><div class="rank">{esc(str(f["rank"]))}</div><div class="fb">'
        f'<div class="fh"><h3>{esc(f["name"])}</h3><span class="tier {TIER.get(f.get("tier"), "t3")}">{esc(f.get("tier", ""))}</span></div>'
        f'<p class="what">{inline(f.get("what", ""))}</p>'
        f'<p class="why"><strong>이어북에 좋은 이유</strong> {inline(f.get("why", ""))}</p>'
        + ('<h4>적용 포인트</h4><ul>' + "".join(f"<li>{inline(x)}</li>" for x in f.get("how", [])) + "</ul>" if f.get("how") else "")
        + (f'<h4>이 기능이 있는 앱</h4><ul class="fapps">{apps}</ul>' if apps else "")
        + f'<p class="evi">근거 · {inline(f.get("evidence", ""))}</p>'
        + (f'<p class="caution">⚠ {inline(f["watch_out"])}</p>' if f.get("watch_out") else "")
        + (f'<p class="techlink"><a href="#tech-{esc(str(f["rank"]))}">기술 구현 보기 ↓</a></p>' if TECH else "")
        + "</div></article>")
section("features", "2. 이어북에 쓰면 좋을 기능 (추천순)", '<div class="feats-list">' + "".join(fs) + "</div>",
        '<p class="lead">조사한 앱들의 기능을 모아, 이어북 사진 선택에 도움이 되는 정도와 근거의 강도로 순위를 매겼다. '
        '<span class="tier t1">필수</span> <span class="tier t2">추천</span> <span class="tier t3">고려</span></p>')


# 3. 기술 구현
if TECH:
    LV = {"확인됨": "t1", "일부 확인": "t2", "공개 근거 없음": "t3"}
    pl = TECH.get("pipeline", {})
    psteps = "".join(
        f'<li><div class="pn">{i + 1}</div><div><strong>{esc(st["name"])}</strong><p>{inline(st.get("detail", ""))}</p>'
        + '<div class="chips2">' + "".join(f'<span class="tchip">{esc(t)}</span>' for t in st.get("tech", [])) + "</div>"
        + ('<div class="serves">쓰는 기능 ' + " ".join(f'<a href="#tech-{n}">{n}</a>' for n in st.get("serves", [])) + "</div>" if st.get("serves") else "")
        + "</div></li>" for i, st in enumerate(pl.get("steps", [])))
    head = (f'<div class="pipe"><h3>{esc(pl.get("title", "공통 분석 파이프라인"))}</h3><p class="lead">{inline(pl.get("lead", ""))}</p>'
            f'<ol class="psteps">{psteps}</ol></div>' if psteps else "")
    if TECH.get("principles"):
        head += '<div class="principles"><h3>전체 원칙</h3><ul>' + "".join(f"<li>{inline(x)}</li>" for x in TECH["principles"]) + "</ul></div>"
    APKS = TECH.get("apk_analyses", [])
    for an in APKS:
        name = f'<a href="#{aid(an["app_ref"])}">{esc(an["app"])}</a>' if an.get("app_ref") in idx else esc(an["app"])
        head += (f'<div class="apkbox"><h3>APK 분석: {name} <span class="sub">{esc(an.get("version", ""))}</span></h3>'
                 f'<dl class="info"><div><dt>출처</dt><dd>{esc(an.get("source", ""))}</dd></div>'
                 f'<div><dt>서명</dt><dd>{esc(an.get("signature", ""))}</dd></div></dl>'
                 '<ul>' + "".join(f"<li>{inline(x)}</li>" for x in an.get("findings", [])) + "</ul>"
                 f'<p class="evi">{esc(an.get("method", ""))}'
                 + (' · 관련 기능 ' + " ".join(f'<a href="#tech-{n}">{n}</a>' for n in an.get("features", [])) if an.get("features") else "")
                 + "</p></div>")
    tcs = []
    for t in TECH.get("features", []):
        def app_link(c):
            if c.get("app_ref") in idx:
                return f'<a href="#{aid(c["app_ref"])}">{esc(c["app"])}</a>'
            return esc(c["app"])

        conf = "".join(
            f'<li><strong>{app_link(c)}</strong> {inline(c.get("what", ""))}'
            + (f' <a class="src" href="{esc(c["source"])}" target="_blank" rel="noopener">출처</a>' if c.get("source") else "")
            + "</li>"
            for c in t.get("confirmed", []))
        tcs.append(
            f'<article class="tech" id="tech-{esc(str(t["rank"]))}"><div class="rank">{esc(str(t["rank"]))}</div><div class="fb">'
            f'<div class="fh"><h3>{esc(t["name"])}</h3><span class="tier {LV.get(t.get("level"), "t3")}">{esc(t.get("level", ""))}</span>'
            f'<a class="back" href="#feat-{esc(str(t["rank"]))}">기능 설명 ↑</a></div>'
            + '<div class="chips2">' + "".join(f'<span class="tchip">{esc(x)}</span>' for x in t.get("stack", [])) + "</div>"
            + (f'<h4>앱에서 확인된 구현</h4><ul>{conf}</ul>' if conf else '<h4>앱에서 확인된 구현</h4><p class="muted">공개 근거 없음</p>')
            + ('<h4>APK 분석으로 확인</h4><ul class="apkf">' + "".join(
                f'<li><strong>{app_link(c)}</strong> {inline(c.get("what", ""))}</li>' for c in t.get("apk_findings", [])) + "</ul>"
               if t.get("apk_findings") else "")
            + '<h4>구현 단계</h4><ol class="isteps">' + "".join(f"<li>{inline(x)}</li>" for x in t.get("steps", [])) + "</ol>"
            + '<div class="tgrid">'
            + f'<div><h4>처리 위치</h4><p>{inline(t.get("where", ""))}</p></div>'
            + ('<div><h4>저장 데이터</h4><ul class="mono">' + "".join(f"<li>{esc(x)}</li>" for x in t.get("data", [])) + "</ul></div>" if t.get("data") else "")
            + "</div>"
            + ('<h4>주의할 점</h4><ul class="cons">' + "".join(f"<li>{inline(x)}</li>" for x in t.get("watch", [])) + "</ul>" if t.get("watch") else "")
            + ('<details class="raw"><summary>APK 분석 때 확인할 단서</summary><ul class="mono">' + "".join(f"<li>{esc(x)}</li>" for x in t.get("apk_checks", [])) + "</ul></details>" if t.get("apk_checks") else "")
            + "</div></article>")
    section("tech", "3. 추천 기능의 기술 구현", head + '<div class="feats-list">' + "".join(tcs) + "</div>",
            '<p class="lead">공개 자료(기술 블로그·논문·특허·도움말·개인정보처리방침·릴리스 노트)로 확인한 구현과, Android에서 만들 때의 권장 구현. '
            '<span class="tier t1">확인됨</span> 앱이 쓴 기술이 공개 근거로 확인 · <span class="tier t2">일부 확인</span> · <span class="tier t3">공개 근거 없음</span> '
            + (f'APK 정적 분석: {len(APKS)}개 앱 ({", ".join(esc(x["app"]) for x in APKS)}).</p>' if APKS else '앱 APK 분석은 아직 하지 않았다.</p>'))

# 0. 읽는 법 + 한눈에 보기 (맨 앞에 넣는다)
if GUIDE:
    types = {t["type"]: t["desc"] for t in GUIDE.get("app_types", [])}
    grid = ""
    for g in order:
        items = [r for r in rows if group_of(r["name"]) == g]
        if not items:
            continue
        tiles = ""
        for r in items:
            md_ = MEDIA.get(r["name"], {})
            ic = (f'<img src="{esc(md_["icon"])}=w80" alt="" loading="lazy" referrerpolicy="no-referrer">' if md_.get("icon")
                  else f'<span class="ph">{esc(short_name(r["name"])[:1])}</span>')
            tiles += (f'<a class="tile" href="#{aid(r["name"])}">{ic}<span><strong>{esc(short_name(r["name"]))}</strong>'
                      f'<small>{inline(profiles.get(r["name"], {}).get("one_liner", ""))}</small></span></a>')
        grid += (f'<div class="tgroup"><h4>{esc(g)} <span class="count">{len(items)}</span></h4>'
                 + (f'<p class="tdesc">{inline(types[g])}</p>' if types.get(g) else "")
                 + f'<div class="tiles">{tiles}</div></div>')
    glossary = "".join(f'<div><dt>{esc(x["term"])}</dt><dd>{inline(x["plain"])}</dd></div>' for x in GUIDE.get("glossary", []))
    intro = (
        '<div class="intro">'
        + (f'<p class="purpose">{inline(GUIDE["purpose"])}</p>' if GUIDE.get("purpose") else "")
        + (f'<p class="question"><span>핵심 질문</span>{inline(GUIDE["question"])}</p>' if GUIDE.get("question") else "")
        + '<div class="igrid"><div><h3>먼저 알면 좋은 결론</h3><ol class="kt">'
        + "".join(f"<li>{inline(x)}</li>" for x in GUIDE.get("key_takeaways", [])) + "</ol></div>"
        + '<div><h3>문서 구성</h3><ul class="parts">'
        + "".join(f'<li><a href="#{["apps", "features", "tech"][i] if i < 3 else "apps"}"><strong>{esc(x["title"])}</strong></a><p>{inline(x["desc"])}</p></li>'
                  for i, x in enumerate(GUIDE.get("parts", [])))
        + "</ul></div></div>"
        + '<div class="legend2"><h3>표시 읽는 법</h3><ul>'
        '<li><span class="actor a-auto">자동</span> 앱이 알아서 처리 · <span class="actor a-mix">자동+확인</span> 앱이 제안하고 사람이 확인 · <span class="actor a-user">사용자</span> 사람이 직접</li>'
        '<li><span class="tier t1">필수</span> <span class="tier t2">추천</span> <span class="tier t3">고려</span> 이어북에 넣을 우선순위</li>'
        '<li><span class="tag unk">미확인</span> 공개 자료로 확인 못 함 · <span class="tag inf">추론</span> 자료를 바탕으로 한 판단 · (APK) 앱 파일을 직접 분석해 확인</li>'
        "</ul></div>"
        f'<h3 class="ov">한눈에 보기: 조사한 앱 {len(rows)}개</h3><p class="lead">아이콘을 누르면 앱 설명으로 이동한다.</p>{grid}'
        + (f'<details class="gloss"><summary>용어 풀이 ({len(GUIDE.get("glossary", []))}개)</summary><dl>{glossary}</dl></details>' if glossary else "")
        + "</div>")
    parts.insert(0, f'<section id="intro"><h2>이 문서 읽는 법</h2>{intro}</section>')
    nav.insert(0, ("intro", "읽는 법"))

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
body{margin:0;background:var(--bg);color:var(--ink);font:16px/1.65 -apple-system,BlinkMacSystemFont,"Apple SD Gothic Neo","Noto Sans KR","Malgun Gothic","Segoe UI",sans-serif;word-break:keep-all;overflow-wrap:break-word}
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
.info{display:grid;grid-template-columns:1fr;gap:8px 14px;margin:0 0 6px;padding:12px 14px;background:var(--bg);border-radius:10px}
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
.feats-list{display:flex;flex-direction:column;gap:14px}
.feat{display:flex;gap:16px;background:var(--panel);border:1px solid var(--line);border-radius:16px;padding:18px 20px}
.rank{flex:none;width:44px;height:44px;border-radius:12px;background:var(--asoft);color:var(--accent);font-weight:800;font-size:20px;display:grid;place-items:center}
.fb{flex:1;min-width:0}.fh{display:flex;gap:8px;align-items:center;flex-wrap:wrap}.fh h3{font-size:18px;margin:0}
.tier{font-size:12px;font-weight:700;border-radius:6px;padding:1px 8px}.tier.t1{background:var(--evs);color:var(--ev)}.tier.t2{background:var(--asoft);color:var(--accent)}.tier.t3{background:var(--soft);color:var(--muted)}
.feat .what{margin:4px 0 8px;color:var(--muted)}.why{margin:0 0 4px;font-size:15px}.why strong{color:var(--accent);margin-right:6px;font-size:13.5px}
.feat h4{font-size:13.5px;color:var(--muted);margin:12px 0 4px}.feat ul{margin:0;padding-left:18px;font-size:14.5px}.feat li{margin:3px 0}
.fapps .an{color:var(--muted);font-size:13.5px}.evi{font-size:13px;color:var(--muted);margin:12px 0 0}
@media (max-width:860px){.feat{padding:14px;gap:12px}.rank{width:36px;height:36px;font-size:17px}}
.techlink{margin:10px 0 0;font-size:13.5px}
.apkbox{background:var(--panel);border:1px solid var(--line);border-left:4px solid var(--ev);border-radius:16px;padding:18px 20px;margin-bottom:14px}
.apkbox h3{font-size:17px;margin:0 0 8px}.apkbox .sub{font-size:13px;color:var(--muted);font-weight:500}.apkbox ul{margin:8px 0 0;padding-left:18px;font-size:14.5px}
.apkf li::marker{color:var(--ev)}
.pipe,.principles{background:var(--panel);border:1px solid var(--line);border-radius:16px;padding:18px 20px;margin-bottom:14px}
.pipe h3,.principles h3{font-size:17px;margin:0 0 4px}.principles ul{margin:6px 0 0;padding-left:18px;font-size:14.5px}
.psteps{list-style:none;padding:0;margin:10px 0 0;display:grid;grid-template-columns:repeat(auto-fill,minmax(230px,1fr));gap:10px}
.psteps li{display:flex;gap:10px;background:var(--bg);border-radius:12px;padding:12px}.psteps p{margin:2px 0 6px;font-size:13.5px;color:var(--muted)}
.pn{flex:none;width:26px;height:26px;border-radius:50%;background:var(--accent);color:#fff;font-size:13px;font-weight:700;display:grid;place-items:center}
.chips2{display:flex;flex-wrap:wrap;gap:5px;margin:8px 0 2px}.tchip{font-size:12px;background:var(--soft);border-radius:6px;padding:2px 8px;font-family:ui-monospace,SFMono-Regular,Menlo,monospace}
.serves{font-size:12px;color:var(--muted);margin-top:6px}.serves a{display:inline-block;min-width:20px;text-align:center;background:var(--asoft);border-radius:5px;margin-left:2px}
.tech{display:flex;gap:16px;background:var(--panel);border:1px solid var(--line);border-radius:16px;padding:18px 20px}
.tech:target,.feat:target{border-color:var(--accent);box-shadow:0 0 0 3px var(--asoft)}
.tech h4{font-size:13.5px;color:var(--muted);margin:14px 0 4px}.tech ul,.tech ol{margin:0;padding-left:20px;font-size:14.5px}.tech li{margin:3px 0}
.back{margin-left:auto;font-size:13px}.tgrid{display:grid;grid-template-columns:1fr 1.4fr;gap:4px 18px}.tgrid p{margin:0;font-size:14.5px}
.mono li{font-family:ui-monospace,SFMono-Regular,Menlo,monospace;font-size:12.5px}
.src{font-size:12px;background:var(--soft);border-radius:5px;padding:0 6px;margin-left:4px}
@media (max-width:860px){.tech{padding:14px;gap:12px}.tgrid{grid-template-columns:1fr}.back{margin-left:0}}
.flow{margin-top:14px}.ftitle{margin:0 0 8px;font-size:13.5px;color:var(--accent);font-weight:600}
.fsteps{list-style:none;counter-reset:fs;padding:0;margin:0;position:relative}
.fsteps li{counter-increment:fs;position:relative;padding:0 0 10px 34px}
.fsteps li::before{content:counter(fs);position:absolute;left:0;top:1px;width:22px;height:22px;border-radius:50%;background:var(--asoft);color:var(--accent);font-size:12px;font-weight:700;display:grid;place-items:center}
.fsteps li:not(:last-child)::after{content:"";position:absolute;left:10.5px;top:25px;bottom:2px;width:1px;background:var(--line)}
.fs-head{display:flex;gap:6px;align-items:center;flex-wrap:wrap}.fs-name{font-weight:600;font-size:14.5px}
.fsteps p{margin:2px 0 0;font-size:14px;color:var(--ink);line-height:1.55}
.actor{font-size:11px;font-weight:700;border-radius:5px;padding:0 6px;line-height:1.7}
.a-auto{background:var(--asoft);color:var(--accent)}.a-user{background:var(--soft);color:var(--muted)}.a-mix{background:var(--evs);color:var(--ev)}
.fbasis{font-size:12.5px;color:var(--muted);margin:2px 0 0}
.chiplist{list-style:none;padding:0!important;display:flex;flex-wrap:wrap;gap:5px}.chiplist li{margin:0!important;font-size:13px;background:var(--soft);border-radius:6px;padding:2px 8px}
.apphead{display:flex;gap:12px;align-items:flex-start}.apphead h3{margin-top:4px}
.appicon{flex:none;width:52px;height:52px;border-radius:12px;border:1px solid var(--line);background:var(--bg);object-fit:cover}
.appicon.ph,.tile .ph{display:grid;place-items:center;font-weight:700;color:var(--muted);font-size:20px}
.plain{margin:12px 0 0;font-size:15px;line-height:1.6;background:var(--bg);border-radius:10px;padding:10px 12px}
.shots{display:flex;gap:8px;overflow-x:auto;margin:12px 0 2px;padding-bottom:6px;scroll-snap-type:x mandatory}
.shots img{flex:none;height:220px;width:auto;border-radius:10px;border:1px solid var(--line);scroll-snap-align:start;background:var(--soft)}
.intro .purpose{font-size:16.5px;line-height:1.7;margin:0 0 10px}
.question{background:var(--asoft);border-radius:12px;padding:12px 16px;margin:0 0 18px;font-weight:600}
.question span{display:inline-block;font-size:12px;color:var(--accent);margin-right:8px;font-weight:700}
.igrid{display:grid;grid-template-columns:1fr 1fr;gap:16px}.igrid>div,.legend2{background:var(--panel);border:1px solid var(--line);border-radius:14px;padding:14px 18px}
.intro h3{font-size:16px;margin:0 0 8px}.kt{margin:0;padding-left:20px;font-size:14.5px}.parts{list-style:none;margin:0;padding-left:0;font-size:14.5px}.kt li,.parts li{margin:5px 0}.parts p{margin:2px 0 0;color:var(--muted);font-size:13.5px}
.legend2{margin-top:14px}.legend2 ul{margin:0;padding-left:18px;font-size:14px}.legend2 li{margin:6px 0}
.ov{font-size:18px!important;margin:26px 0 4px!important}
.tgroup{margin:14px 0}.tgroup h4{font-size:14.5px;margin:0 0 2px}.tdesc{margin:0 0 8px;font-size:13.5px;color:var(--muted)}
.tiles{display:grid;grid-template-columns:repeat(auto-fill,minmax(230px,1fr));gap:8px}
.tile{display:flex;gap:10px;align-items:center;background:var(--panel);border:1px solid var(--line);border-radius:12px;padding:8px 10px;color:var(--ink)}
.tile:hover{border-color:var(--accent);text-decoration:none}.tile img,.tile .ph{flex:none;width:40px;height:40px;border-radius:9px;border:1px solid var(--line)}
.tile span{display:flex;flex-direction:column;min-width:0}.tile strong{font-size:14px}.tile small{font-size:12px;color:var(--muted);line-height:1.4}
.gloss{background:var(--panel);border:1px solid var(--line);border-radius:14px;margin-top:16px}.gloss summary{padding:12px 16px;cursor:pointer;font-weight:600}
.gloss dl{display:grid;grid-template-columns:repeat(auto-fill,minmax(300px,1fr));gap:8px 18px;padding:0 18px 16px;margin:0}
.gloss dt{font-weight:700;font-size:14px}.gloss dd{margin:2px 0 0;font-size:13.5px;color:var(--muted)}
@media (max-width:860px){.igrid{grid-template-columns:1fr}.shots img{height:180px}}
.muted{color:var(--muted);font-size:13px}
.theme{position:fixed;right:16px;bottom:16px;border:1px solid var(--line);background:var(--panel);color:var(--ink);border-radius:999px;padding:8px 14px;font:inherit;font-size:13px;cursor:pointer}
footer{color:var(--muted);font-size:13px;text-align:center}
@media (max-width:860px){main{padding:20px 16px 72px}.top nav{padding:8px 12px}.hero h1{font-size:24px}.apps{grid-template-columns:minmax(0,1fr)}
.app{padding:16px}.info{grid-template-columns:1fr}.summary{padding:14px 16px 14px 36px}}
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
