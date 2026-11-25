"""이전 research 실행의 journal.jsonl에서 대상별 raw 결과를 뽑아 merge 모드에 넘길 JSON 배열을 만든다.

사용법: python3 -I raw_from_journal.py <journal.jsonl> [<journal.jsonl> ...] > raw.json

각 항목은 {target: {name}, collected, checks} 형태로, 워크플로의 research 결과 `raw`와 같다.
같은 대상이 여러 journal에 있으면 뒤에 준 파일의 결과가 이긴다.
"""
import json
import sys


def load(path):
    label_of = {}
    results = {}
    with open(path, encoding="utf-8") as f:
        for line in f:
            d = json.loads(line)
            if d.get("type") == "started" and d.get("label"):
                label_of[d["key"]] = d["label"]
            elif d.get("type") == "result":
                results[d["key"]] = d.get("result")
    collected, checks = {}, {}
    for key, label in label_of.items():
        if key not in results or results[key] is None:
            continue
        kind, _, name = label.partition(":")
        if kind == "collect":
            collected[name] = results[key]
        elif kind == "verify":
            checks[name] = (results[key] or {}).get("checks", [])
    return [
        {"target": {"name": name}, "collected": col, "checks": checks.get(name, [])}
        for name, col in collected.items()
    ]


def main():
    merged = {}
    for path in sys.argv[1:]:
        for item in load(path):
            merged[item["target"]["name"]] = item
    json.dump(list(merged.values()), sys.stdout, ensure_ascii=False)


if __name__ == "__main__":
    main()
