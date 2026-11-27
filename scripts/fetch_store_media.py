"""links.json의 Google Play 패키지마다 앱 아이콘과 스크린샷 이미지 주소를 모아 media.json으로 저장한다.

사용법: python3 scripts/fetch_store_media.py <merge-dir> [최대 스크린샷 수, 기본 4]

이미지 파일은 내려받지 않고 Google Play 이미지 주소만 저장한다(보고서에서 그 주소로 불러온다).
"""
import json
import re
import subprocess
import sys
from pathlib import Path

d = Path(sys.argv[1])
max_shots = int(sys.argv[2]) if len(sys.argv) > 2 else 4
links = json.loads((d / "links.json").read_text(encoding="utf-8"))
out = {}
for name, L in links.items():
    pkg = L.get("play")
    if not pkg:
        continue
    url = f"https://play.google.com/store/apps/details?id={pkg}&hl=ko&gl=KR"
    html = subprocess.run(["curl", "-s", "-m", "30", "-A", "Mozilla/5.0", url],
                          capture_output=True, text=True).stdout
    imgs = re.findall(r'<img[^>]+src="(https://play-lh\.googleusercontent\.com/[^"=]+)[^"]*"[^>]*alt="([^"]*)"', html)
    icon = next((u for u, a in imgs if "아이콘" in a), None)
    shots = []
    for u, a in imgs:
        if "스크린샷" in a and u not in shots:
            shots.append(u)
    out[name] = {"icon": icon, "shots": shots[:max_shots]}
    print(f"{len(shots[:max_shots])} shots, icon={'y' if icon else 'n'}  {name}")
(d / "media.json").write_text(json.dumps(out, ensure_ascii=False, indent=2), encoding="utf-8")
print("저장:", d / "media.json")
