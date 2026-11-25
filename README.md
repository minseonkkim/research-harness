# research-harness

양식(템플릿)을 정하고 → 에이전트가 리서치하고 → 문서로 채우는 Claude Code 리서치 하네스.

## 구성

```
.claude/
  skills/research-doc/SKILL.md     # 진행 절차 (Claude가 따르는 지침)
  workflows/research-doc.js        # 조사 → 검증 → 작성 워크플로
templates/
  competitor-apps.json             # 경쟁 앱 조사 양식
  feature-benchmark.json           # 기능 벤치마크 양식
scripts/
  fetch.sh, html2text.py           # 페이지 본문 추출 (WebFetch 대체 경로)
reports/                           # 생성된 보고서
```

## 흐름

1. **입력**: 주제, 관점(조사 결과를 어디에 쓰는지), 양식, 대상
2. **Discover** (선택): 비슷한 대상 후보 찾기 → 사용자가 목록 확정
3. **Collect**: 대상마다 에이전트 1명이 양식의 모든 항목을 출처와 함께 채움
4. **Verify**: `verify: true` 항목을 다른 에이전트가 독립적으로 확인·수정
5. **Synthesize**: 요약, 패턴, 시사점 섹션 작성 (근거와 추론을 구분)
6. **Render**: 비교표, 미확인 목록, 대상별 부록을 붙여 `reports/`에 저장

## 사용

이 저장소를 연 Claude Code 세션에서:

```
/research-doc 아이 사진 정리 앱 조사. Bebememo, 쑥쑥찰칵 포함하고 비슷한 앱도 찾아줘.
관점: 이어북 편집기 사진 선택 단계 기획
```

## 비용 감각

대상 1개당 에이전트 약 2개(조사 + 검증), 그 외 discover 3개와 작성 1개.
대상 8개면 에이전트 20개 안팎이다.
