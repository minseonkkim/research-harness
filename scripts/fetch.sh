#!/usr/bin/env bash
# 웹 페이지를 받아 본문 텍스트만 출력한다.
# WebFetch 도구가 프록시 환경에서 실패할 때 쓰는 대체 경로다.
#
# 사용법: bash scripts/fetch.sh <URL> [최대 글자 수, 기본 12000]
set -euo pipefail

url="${1:?URL이 필요합니다}"
max="${2:-12000}"
here="$(cd "$(dirname "$0")" && pwd)"

tmp="$(mktemp -d)"
trap 'rm -rf "$tmp"' EXIT

if ! curl -sSL --compressed -m 30 --retry 2 \
     -A "Mozilla/5.0 (research-harness)" \
     -o "$tmp/page.html" -w "%{http_code}" "$url" > "$tmp/code"; then
  echo "[fetch 실패] $url (네트워크 오류)" >&2
  exit 2
fi

code="$(cat "$tmp/code")"
if [ "$code" -ge 400 ]; then
  echo "[fetch 실패] $url (HTTP $code)" >&2
  exit 3
fi

python3 -I "$here/html2text.py" "$tmp/page.html" "$max"
