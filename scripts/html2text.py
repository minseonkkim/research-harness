"""HTML 파일에서 본문 텍스트만 뽑아 표준 출력으로 내보낸다.

사용법: python3 -I html2text.py <파일> [최대 글자 수]
"""
import re
import sys
from html.parser import HTMLParser

SKIP = {"script", "style", "noscript", "svg", "nav", "footer", "header", "form"}
BLOCK = {"p", "br", "li", "h1", "h2", "h3", "h4", "h5", "div", "tr", "section", "article"}


class Extractor(HTMLParser):
    def __init__(self):
        super().__init__()
        self.out = []
        self.skip = 0
        self.title = ""
        self._in_title = False

    def handle_starttag(self, tag, attrs):
        if tag in SKIP:
            self.skip += 1
        if tag == "title":
            self._in_title = True
        if tag in BLOCK:
            self.out.append("\n")

    def handle_endtag(self, tag):
        if tag in SKIP and self.skip:
            self.skip -= 1
        if tag == "title":
            self._in_title = False

    def handle_data(self, data):
        if self._in_title:
            self.title += data
        if not self.skip:
            self.out.append(data)


def main():
    path = sys.argv[1]
    limit = int(sys.argv[2]) if len(sys.argv) > 2 else 12000
    p = Extractor()
    with open(path, encoding="utf-8", errors="ignore") as f:
        p.feed(f.read())
    text = re.sub(r"[ \t]+", " ", "".join(p.out))
    lines = [ln.strip() for ln in text.splitlines()]
    lines = [ln for ln in lines if len(ln) > 1]
    body = "\n".join(lines)
    if len(body) < 200:
        print("[경고] 본문이 거의 없습니다. 봇 차단이나 JS 렌더링 페이지일 수 있습니다.")
    print(f"# {p.title.strip()}\n")
    print(body[:limit])
    if len(body) > limit:
        print(f"\n[... {len(body) - limit}자 생략]")


if __name__ == "__main__":
    main()
