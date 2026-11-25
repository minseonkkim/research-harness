---
name: research-doc
description: 양식(템플릿) 기반 리서치 하네스. 여러 앱·제품·서비스를 같은 항목으로 조사해 출처가 달린 문서로 만든다. "~앱 리서치해서 정리해줘", "경쟁 앱 조사", "기능 벤치마크", "이 앱들이랑 비슷한 거 찾아서 문서로" 같은 요청에 사용한다.
---

# research-doc: 양식 → 리서치 → 문서

이 저장소의 `templates/*.json` 양식으로 조사 항목을 정하고, `.claude/workflows/research-doc.js` 워크플로로 조사·검증·작성을 돌린 뒤, `reports/`에 Markdown 문서를 남긴다.

## 1. 입력 정리 (사용자에게 확인)

다음 네 가지가 정해져야 시작한다. 빠진 것만 짧게 묻는다.

- **주제(topic)**: 무엇을 조사하나. 예: "아이 사진 정리·앨범 앱"
- **관점(lens)**: 조사 결과를 어디에 쓰나. 예: "이어북 편집기의 사진 선택 단계 기획". 관점이 구체적일수록 시사점이 좋아진다.
- **양식(template)**: `templates/` 중 선택. 없으면 아래 "새 양식 만들기"로 만든다.
  - `competitor-apps`: 앱 여러 개를 같은 항목으로 비교
  - `feature-benchmark`: 특정 기능 하나의 구현 방식 비교
- **대상(targets)**: 사용자가 이름을 준 대상 + 비슷한 대상을 더 찾을지 여부

## 2. 대상 확정 (discover → 사용자 확인)

사용자가 준 대상만으로 충분하면 건너뛴다. 비슷한 대상을 더 찾아야 하면:

```
Workflow({
  scriptPath: "<저장소>/.claude/workflows/research-doc.js",
  args: { mode: "discover", template: <양식 JSON>, topic, lens,
          seeds: ["사용자가 준 대상들"], harnessDir: "<저장소 절대경로>", date: "<오늘>" }
})
```

결과 후보를 표로 보여주고 **사용자에게 대상 목록을 확정받는다.** 특히:
- `confident: false` 후보나 사용자가 준 이름 중 특정이 애매한 것(동명 앱, 오타 의심)은 스토어 링크나 개발사를 물어본다.
- 대상은 보통 5~10개. 많을수록 비용이 선형으로 늘어난다(대상당 에이전트 2개).

## 3. 리서치 실행

```
Workflow({
  scriptPath: "<저장소>/.claude/workflows/research-doc.js",
  args: { mode: "research", template: <양식 JSON>, topic, lens,
          targets: [{ name, hint }],   // hint: 개발사·스토어 링크 등 식별 정보
          harnessDir: "<저장소 절대경로>", date: "<오늘>" }
})
```

- `template`은 양식 파일 내용을 JSON 값 그대로 넘긴다(문자열로 감싸지 않는다). 워크플로는 파일을 읽을 수 없다.
- 단계: Collect(대상당 1명) → Verify(`verify: true` 항목만 독립 검증) → Synthesize(요약·패턴·시사점 작성) → 스크립트가 표와 부록을 렌더링.

## 4. 문서 저장과 보고

1. 결과의 `markdown`을 `reports/<YYYY-MM-DD>-<주제-슬러그>.md`로, 결과의 `raw`를 `reports/data/<같은 이름>.raw.json`으로 저장하고 커밋·푸시한다. raw가 있어야 나중에 합칠 수 있다. raw를 잃었으면 `python3 -I scripts/raw_from_journal.py <journal.jsonl>...`로 실행 기록에서 복원한다.
2. 사용자에게는 핵심 요약, 시사점, `unverified`(특정 실패한 대상 포함)를 짧게 전한다. 문서 전체를 채팅에 붙이지 않는다.
3. 사용자가 원하면 Notion이나 Claude Docs로 옮긴다.

## 5. 여러 번의 조사를 한 보고서로 합치기

대상을 나눠 조사했거나 나중에 추가했을 때, 다시 조사하지 않고 합친 보고서를 만든다.

1. `node scripts/merge_report.mjs prepare templates/<양식>.json reports/data/merge-<날짜> reports/data/a.raw.json reports/data/b.raw.json ... --topic "..." --lens "..." --date <오늘>`
2. 에이전트 1개(general-purpose)에게 `reports/data/merge-<날짜>/synth-input.md`를 읽고 지시대로 `sections.json`을 쓰게 한다. 대상이 많으면 유형별로 묶어 쓰라고, 앱 규모(검증 정도)에 따라 근거 무게를 구분하라고 덧붙인다.
3. `node scripts/merge_report.mjs render templates/<양식>.json reports/data/merge-<날짜> reports/<날짜>-<슬러그>-merged.md --topic "..." --lens "..." --date <오늘>`

raw가 작으면(수십 KB) 워크플로 `mode: "merge", raw: [...]`로도 된다.

## 실패했을 때

- 결과가 비었거나 이상하면 워크플로의 `journal.jsonl`부터 읽는다.
- 페이지 읽기가 전부 실패하면: `bash scripts/fetch.sh <URL>`을 직접 실행해 네트워크를 확인한다. 막혔으면 환경 네트워크 설정 문제다.
- 일부 대상만 실패했으면 그 대상만 `targets`로 다시 돌리고 문서를 합친다.

## 새 양식 만들기

`templates/<id>.json`에 아래 구조로 만든다.

```json
{
  "id": "market-scan",
  "title": "시장 조사",
  "fields": [
    { "key": "필드키", "label": "표시 이름", "desc": "조사자에게 주는 설명", "verify": true }
  ],
  "sections": [
    { "key": "summary", "title": "요약", "prompt": "합성 에이전트에게 주는 작성 지시" },
    { "key": "comparison", "title": "비교표", "builtin": "table", "fields": ["필드키"] },
    { "key": "gaps", "title": "확인하지 못한 것", "builtin": "unverified" }
  ]
}
```

- `verify: true`는 틀리면 결론이 흔들리는 항목(정체, 수치, 가격, 관점 핵심 기능)에만 붙인다. 많을수록 검증 비용이 는다.
- `builtin: "table"`은 스크립트가 데이터로 바로 그리고, `prompt` 섹션은 합성 에이전트가 쓴다.
