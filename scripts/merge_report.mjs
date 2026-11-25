#!/usr/bin/env node
// 저장해 둔 raw 데이터(reports/data/*.raw.json) 여러 개를 합쳐 통합 보고서를 만든다.
// 워크플로 merge 모드는 raw를 인자로 받아야 해서 데이터가 크면 쓰기 어렵다. 이 스크립트는 파일로 처리한다.
//
// 1) 준비:  node scripts/merge_report.mjs prepare <template.json> <out-dir> <raw1.json> [raw2.json ...] --topic "..." --lens "..." --date YYYY-MM-DD
//           → <out-dir>/rows.json (검증 반영된 대상별 데이터), <out-dir>/synth-input.md (작성 에이전트용 지시+데이터)
// 2) 작성:  에이전트가 synth-input.md를 읽고 <out-dir>/sections.json 에 [{key, markdown}] 를 쓴다.
// 3) 렌더:  node scripts/merge_report.mjs render <template.json> <out-dir> <report.md> --topic "..." --lens "..." --date YYYY-MM-DD
//
// 검증 반영과 렌더링 규칙은 .claude/workflows/research-doc.js 와 같다. 한쪽을 고치면 다른 쪽도 맞춘다.
import fs from 'node:fs'
import path from 'node:path'

const [cmd, templatePath, outDir, ...rest] = process.argv.slice(2)
if (!cmd || !templatePath || !outDir) {
  console.error('사용법은 파일 상단 주석 참고')
  process.exit(1)
}
const T = JSON.parse(fs.readFileSync(templatePath, 'utf8'))
const verifyKeys = T.fields.filter(f => f.verify).map(f => f.key)
const cell = s => String(s == null ? '' : s).replace(/\|/g, '/').replace(/\s*\n\s*/g, ' ').trim()

function applyVerification(results) {
  const rows = []
  const unverified = []
  for (const r of results) {
    const name = r.target.name
    if (!r.collected) { unverified.push(name + ': 조사 에이전트가 결과를 반환하지 않음'); continue }
    if (!r.collected.identified) {
      unverified.push(name + ': 대상을 특정하지 못함 — ' + cell(r.collected.identity_note))
      rows.push({ name, identified: false, note: r.collected.identity_note, fields: {} })
      continue
    }
    const fields = {}
    for (const f of r.collected.fields) fields[f.key] = { ...f, status: verifyKeys.includes(f.key) ? 'unchecked' : 'n/a' }
    for (const c of r.checks || []) {
      const f = fields[c.key]
      if (!f) continue
      if (c.verdict === 'confirmed') f.status = 'confirmed'
      if (c.verdict === 'corrected') {
        f.status = 'corrected'
        f.note = ((f.note || '') + ' [검증에서 수정: 원래 값 "' + cell(f.value) + '"]').trim()
        f.value = c.corrected_value || f.value
        if (c.source) f.sources = [c.source, ...(f.sources || [])]
      }
      if (c.verdict === 'unverifiable') {
        f.status = 'unverifiable'
        f.confidence = 'low'
        unverified.push(name + ' / ' + c.key + ': ' + cell(c.reason))
      }
    }
    for (const f of Object.values(fields)) {
      if (String(f.value).trim() === '미확인') unverified.push(name + ' / ' + f.key + ': 미확인')
    }
    for (const q of r.collected.open_questions || []) unverified.push(name + ': ' + cell(q))
    rows.push({ name, identified: true, note: r.collected.identity_note, extra: r.collected.extra, fields })
  }
  return { rows, unverified }
}

function opt(name) {
  const i = rest.indexOf('--' + name)
  return i >= 0 ? rest[i + 1] : ''
}

if (cmd === 'prepare') {
  const raw = []
  const seen = new Set()
  const files = rest.slice(0, rest.findIndex(a => a.startsWith('--')) >>> 0 || rest.length).filter(a => !a.startsWith('--'))
  for (const p of files) {
    for (const r of JSON.parse(fs.readFileSync(p, 'utf8'))) {
      if (seen.has(r.target.name)) continue
      seen.add(r.target.name)
      raw.push(r)
    }
  }
  const { rows, unverified } = applyVerification(raw)
  fs.mkdirSync(outDir, { recursive: true })
  fs.writeFileSync(path.join(outDir, 'rows.json'), JSON.stringify({ rows, unverified }, null, 0))
  const data = JSON.stringify(rows.map(r => ({
    name: r.name, identified: r.identified, extra: r.extra,
    fields: Object.fromEntries(Object.entries(r.fields).map(([k, f]) => [k, { value: f.value, confidence: f.confidence, status: f.status, note: f.note }])),
  })))
  const prose = (T.sections || []).filter(s => s.prompt)
  const input =
    '## 보고서 섹션 작성\n' +
    '조사 주제: ' + opt('topic') + '\n조사 관점(lens): ' + opt('lens') + '\n기준일: ' + (opt('date') || '(날짜 미지정)') + '\n\n' +
    '아래는 검증을 거친 조사 데이터다(JSON). 이 데이터만 근거로 섹션을 쓴다. 새 사실을 지어내지 않는다. ' +
    'status가 unverifiable이거나 confidence가 low인 값에 기대는 문장은 "(미확인)"을 붙인다. ' +
    '추론은 "(추론)"으로 표시한다. 한국어, 간결한 Markdown(섹션 제목 없이 본문만).\n\n' +
    '## 쓸 섹션\n' + prose.map(s => '- key `' + s.key + '` — ' + s.title + ': ' + s.prompt).join('\n') + '\n\n' +
    '## 출력\n' + path.join(outDir, 'sections.json') + ' 에 [{"key": "...", "markdown": "..."}] JSON 배열로 쓴다.\n\n' +
    '## 데이터\n' + data + '\n'
  fs.writeFileSync(path.join(outDir, 'synth-input.md'), input)
  console.log(`대상 ${rows.length}개, 미확인 ${unverified.length}개 → ${outDir}/rows.json, synth-input.md (${input.length}자)`)
} else if (cmd === 'render') {
  const [reportPath] = rest
  const { rows, unverified } = JSON.parse(fs.readFileSync(path.join(outDir, 'rows.json'), 'utf8'))
  const sections = JSON.parse(fs.readFileSync(path.join(outDir, 'sections.json'), 'utf8'))
  const prosed = Object.fromEntries(sections.map(s => [s.key, s.markdown]))
  const label = Object.fromEntries(T.fields.map(f => [f.key, f.label]))
  const mark = f => !f ? '' : f.status === 'confirmed' ? ' ✓' : f.status === 'corrected' ? ' ✎' : f.status === 'unverifiable' ? ' ?' : ''
  const out = []
  out.push('# ' + T.title + ': ' + opt('topic'), '')
  out.push('- 관점: ' + opt('lens'), '- 기준일: ' + (opt('date') || '(날짜 미지정)'), '- 대상 (' + rows.length + '개): ' + rows.map(r => r.name).join(', '), '')
  out.push('> 표기: ✓ 독립 검증 확인 · ✎ 검증에서 수정 · ? 검증 불가', '')
  for (const s of T.sections || []) {
    out.push('## ' + s.title, '')
    if (s.builtin === 'table') {
      const keys = s.fields || T.fields.map(f => f.key)
      out.push('| 대상 | ' + keys.map(k => label[k] || k).join(' | ') + ' |')
      out.push('|---|' + keys.map(() => '---').join('|') + '|')
      for (const r of rows) {
        if (!r.identified) { out.push('| ' + cell(r.name) + ' | ' + keys.map(() => '특정 실패').join(' | ') + ' |'); continue }
        out.push('| ' + cell(r.name) + ' | ' + keys.map(k => cell(r.fields[k] && (r.fields[k].short || r.fields[k].value)) + mark(r.fields[k])).join(' | ') + ' |')
      }
      out.push('', '_자세한 내용과 출처는 부록 참고._', '')
    } else if (s.builtin === 'unverified') {
      out.push(unverified.length ? unverified.map(u => '- ' + u).join('\n') : '- 없음', '')
    } else {
      out.push(prosed[s.key] || '_(작성되지 않음)_', '')
    }
  }
  out.push('## 부록: 대상별 상세', '')
  for (const r of rows) {
    out.push('### ' + r.name, '')
    if (!r.identified) { out.push('특정하지 못함: ' + r.note, ''); continue }
    for (const f of T.fields) {
      const v = r.fields[f.key]
      if (!v) continue
      const src = (v.sources || []).map((u, i) => '[' + (i + 1) + '](' + u + ')').join(' ')
      out.push('- **' + f.label + '**' + mark(v) + ': ' + cell(v.value) + (v.note ? ' _(' + cell(v.note) + ')_' : '') + (src ? ' ' + src : ''))
    }
    if (r.extra) out.push('- **기타**: ' + cell(r.extra))
    out.push('')
  }
  fs.writeFileSync(reportPath, out.join('\n'))
  console.log('저장: ' + reportPath)
} else {
  console.error('알 수 없는 명령: ' + cmd)
  process.exit(1)
}
