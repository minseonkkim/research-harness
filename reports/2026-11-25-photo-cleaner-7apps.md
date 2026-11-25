# 경쟁 앱 조사: 안드로이드(Google Play) 사진 정리 앱: 아이 성장 앨범 앱과 범용 갤러리·정리 앱 (포토북 전문 서비스는 제외)

- 관점: yearbook(연간 포토북) 편집기의 사진 선택 단계 기획: 1년치 사진 중 책에 넣을 사진을 고르는 화면과 흐름. 각 앱의 '사진 정리' 기능(자동 분류, 인물·아이 인식, 유사·중복 묶기, 베스트컷 추천, 즐겨찾기·필터, 스와이프 선별 등)이 실제로 어떻게 동작하는지 중심으로 본다.
- 기준일: 2026-11-25
- 대상: BestCut: AI Photo Selection, 사진쏙 - 중복·유사 사진 정리, 베스트컷 - 중복사진 정리 & 갤러리 용량 확보, 사진정리 한방 - 중복 사진·동영상 한번에 삭제, 키즈로그 - 사진분류, 알림장, 보육일지, Sponge - Gallery Cleaner, Favvy: Clean your photos

> 표기: ✓ 독립 검증 확인 · ✎ 검증에서 수정 · ? 검증 불가

## 요약

- 조사한 7개 앱 중 6개는 **'지울 사진 고르기'(용량 확보)** 도구다. 나머지 1개(키즈로그)는 교사용 아이별 분류 도구다. 1년치 사진에서 '책에 넣을 사진'을 고르는 흐름을 그대로 갖춘 앱은 없었다. 부모용 아이 성장 앨범 앱도 이번 대상에는 없다.
- 사진 선택 단계에 옮겨 쓸 만한 패턴은 네 가지다. ① 시간·장소·시각 유사도로 비슷한 사진을 묶고 대표 1장을 추천한다(BestCut, 사진쏙, 베스트컷, 사진정리 한방). ② 월 단위로 나눠 유지/제외를 스와이프로 정하고 진행률을 보여 준다(Sponge, Favvy). ③ 얼굴·즐겨찾기를 '남길 사진' 신호로 쓴다(사진쏙, 사진정리 한방). ④ 인물별로 자동 분류하고 사용자가 고치면 다시 학습한다(키즈로그).
- 시장에서 검증된 앱은 Sponge(Play 평점 4.7, 50만+ 다운로드)와 Favvy(5만+) 둘뿐이다. 둘 다 AI 선별 기능이 없거나 약하다. Sponge 사용자는 중복·유사 묶기를, Favvy 사용자는 인물별 정렬을 요청하고 있다. AI 묶기·추천 앱은 다운로드 10~100+ 수준의 신생 개인 앱이라 품질이 검증되지 않았다.
- 처리 방식은 대체로 온디바이스 분석이다(자사 주장). 서버에서 처리하는 앱은 키즈로그 하나다(InsightFace 얼굴 임베딩).

## 비교표

| 대상 | 개발사·국가 | 평점·규모 | 관점 관련 기능 | 가격 모델 |
|---|---|---|---|---|
| BestCut: AI Photo Selection | basicworld (개인 개발자 추정, 한국 창원) ✓ | 다운로드 100+, 평점 미표시 ✓ | 시간·각도로 유사사진 묶음 → 묶음별 베스트컷 추천 → 좋아요/휴지통 ✓ | 무료+광고, 인앱 구매 있음(가격 미확인) ✓ |
| 사진쏙 - 중복·유사 사진 정리 | 마중물(BoazHwang), 한국 성남, 개인사업자로 추정 ✓ | 다운로드 10+, 평점 없음, 2026-10 업데이트 ✓ | 유사 그룹별 베스트컷 자동 추천, 보관/정리 버튼으로 선별 ✓ | 무료, 광고 포함, 인앱 구매 표기 없음 ✓ |
| 베스트컷 - 중복사진 정리 & 갤러리 용량 확보 | poty.(개인 개발자 이종언), 한국 ✓ | 다운로드 10+, 평점 없음 ✓ | GPS 50m·2분 시간창과 pHash로 묶은 뒤 사용자가 남길 컷 선택 ✎ | 무료(광고 포함), 인앱결제 표시 없음 ✓ |
| 사진정리 한방 - 중복 사진·동영상 한번에 삭제 | 개인 개발자 이정호(hoi79), 한국 김포 ✓ | 다운로드 10+, 평점 없음(2026-11-24 출시) ✓ | 삭제용 자동 분류+선명컷 추천, 얼굴·즐겨찾기 보호 ✓ | 무료(500MB)+광고 보고 1GB 추가, 인앱 ₩2,500~3,900 ✓ |
| 키즈로그 - 사진분류, 알림장, 보육일지 | 셀리(개인사업자, 대표 이현준) / 한국 ✓ | Play 1천+ 다운로드, App Store 5.0(4개) — 초기 단계 ✓ | 이름등록→최대100장 업로드→얼굴인식 아이별 분류·갤러리 폴더 저장, 수동 이동으로 보정 ✓ | 구독: Light 4,900 / Basic 9,900 / Pro 19,900원/월, 분류는 무제한 ✓ |
| Sponge - Gallery Cleaner | PRISMTREE, 인도(델리) 인디 개발사 ✓ | Play 4.7(6.25천), 50만+ 다운로드 ✓ | 월·앨범별 수동 스와이프 선별, AI 묶기·추천 없음 ✓ | 무료+Premium(iOS 연 $9.99/평생 $14.99) ✓ |
| Favvy: Clean your photos | Kaiku Labs (The Software Company of Barcelona S.L., 스페인) ✓ | Play 3.6★(816), 5만+ 다운로드. iOS 미국 4.7★(95) ✓ | 월·카테고리 필터 + 1장씩 좌우 스와이프 + 세션 끝 일괄 검토. 인물 인식·베스트컷 없음 ✓ | 부분 무료 + PRO 구독(미국 iOS 주 $4.99~연 $34.99) ✓ |

_자세한 내용과 출처는 부록 참고._

## 관점별 기능 패턴

**1. 유사·연속 촬영 사진 묶기 → 묶음별 대표 1장 추천**
- BestCut: 비슷한 시간대·각도의 사진을 AI로 묶고 묶음마다 '베스트 컷'을 추천한다. 추천 기준은 공개되지 않았다.
- 사진쏙: 유사 사진을 묶고 선명도·눈 뜬 표정·미소를 기준으로 베스트컷을 추천한다. 흐린 사진과 눈 감은 사진은 따로 후보로 표시한다.
- 사진정리 한방: 연사 묶음에서 '가장 선명한 한 장'을, 중복 묶음에서 남길 1장을 추천한다.
- 베스트컷(poty.): 묶는 규칙이 가장 구체적이다. GPS 50m 이내 또는 촬영 시간 2분 이내 사진을 후보로 모은 뒤 지각적 해시로 확정한다. 자동 추천은 없고 사람이 직접 고른다.
- Favvy: Duplicates 모드로 유사 사진을 묶는다(2026년 6월 추가). 이후 업데이트에서 '관련 없는 사진까지 묶던 문제'를 수정했다.

**2. 자동 추천, 최종 확정은 사용자**
- 위 앱들 모두 묶기와 추천은 자동으로 하고, 남길지 말지는 사용자가 확정한다. 사진쏙 설명에는 '어떤 사진을 지울지는 항상 직접 확인하고 결정'한다고 적혀 있다.
- 묶음 구성이 틀렸을 때 고치는 수단이 있다. BestCut은 탭으로 사진을 넣고 뺀다. 키즈로그는 사진을 다른 아이로 옮기면 다음부터 따로 인식한다.

**3. 이진 결정(유지/제외) UI**
- 스와이프 카드: Sponge(왼쪽 삭제/오른쪽 유지, 버튼으로도 가능), Favvy(좌우 스와이프, 세션 끝에 삭제 더미를 검토한 뒤 확정, Undo 가능).
- 그룹 단위 버튼: 사진쏙 v1.3은 베스트샷을 크게 보여 주고 보관/정리 버튼과 되돌리기를 둔다.
- 비교 화면: 베스트컷(poty.)은 두 장을 나란히 놓고 버튼을 길게 누르면 다른 사진으로 바꿔 보여 준다(1:1 비교). 그룹 그리드에서는 남길 사진을 탭한다.

**4. 많은 양을 나눠서 처리**
- 월별 분할: Sponge와 Favvy 모두 월별 모드가 있다.
- 작은 묶음 단위: Sponge 무작위 모드는 30/50/100장씩 끊어 보여 준다.
- 진행률과 이어하기: Sponge는 월·앨범마다 체크리스트식으로 진행 상태를 표시하고 중단한 지점부터 이어 한다. Favvy는 이미 본 사진을 다시 보여 주지 않고, 스트릭 보상도 있다.
- 범위 지정: 베스트컷(poty.)은 날짜 범위를 골라 그 기간만 스캔한다.
- 증분 분석: 사진정리 한방은 처음 한 번 전체를 분석한 뒤에는 새로 찍은 사진만 반영한다.

**5. '제외할 사진' 자동 분류**
- 사진정리 한방: 스크린샷, 흔들린 사진, 영수증·서류(글자가 많은 사진), 대용량 동영상을 자동으로 분류한다.
- 사진쏙: 흐린 사진과 눈 감은 사진을 표시한다.
- Favvy: 흐린·어두운·저화질 사진 정리가 Play 설명에만 있다. 실제로 자동 감지하는지는 확인하지 못했다(미확인).
- Sponge·Favvy: 스크린샷, 동영상 같은 미디어 유형별 모드가 있다.

**6. 얼굴·즐겨찾기를 신호로 사용**
- 사진정리 한방: 얼굴이 나온 사진과 갤러리 즐겨찾기(하트) 사진은 정리 대상에서 뺀다.
- 사진쏙: 즐겨찾기, 인물, 최근, 클라우드에만 있는 사진이 삭제 대상에 들어 있으면 먼저 경고한다.
- BestCut: 앱에서 '좋아요'한 사진을 기기 기본 갤러리 즐겨찾기에 동기화한다.

**7. 인물(아이)별 자동 분류**
- 키즈로그만 해당한다. 아이 이름을 한 번 등록하고 최대 100장을 올리면 서버가 얼굴을 인식해 아이별로 나눈다(예시: '민준 12장/서아 9장/단체사진 5장'). 단체사진은 함께 나온 아이 모두에게 들어간다. 결과는 기기 갤러리의 아이별 폴더로 저장된다.
- 나머지 6개 앱에는 인물별 분류가 없다. Favvy 후기에는 인물별 정렬 요청이 실려 있다.

**공통 한계**: 결과가 '삭제' 또는 '폴더 이동'으로 끝난다. 고른 사진을 '선택 목록'으로 남기는 앱은 없다. BestCut의 즐겨찾기 동기화와 키즈로그의 아이별 폴더가 그나마 가깝다.

## 기획 시사점

**근거가 있는 제안**
- **월 단위로 나눠 고르고 진행률 보여 주기**: 1년치를 12개월로 나눠 보여 주고, 달마다 진행 상태(고른 장수, 검토 완료 여부)와 이어하기를 둔다. 근거: Sponge와 Favvy의 월별 모드·체크리스트·이어하기. 특히 Sponge는 AI 없이 이 구조만으로 평점 4.7, 50만+ 다운로드를 얻었다.
- **유사 사진 묶음 → 대표 1장 자동 추천 → 사용자 확정**: 연속 촬영 사진을 묶음 하나로 접고 대표컷만 기본으로 보여 준다. 묶는 규칙은 베스트컷(poty.)의 '촬영 시간 2분·GPS 50m 이내로 후보를 모은 뒤 시각 유사도로 확정'을 출발점으로 쓸 수 있다. 대표컷 기준은 사진쏙(선명도·눈 뜬 표정·미소)과 사진정리 한방(선명도)을 참고한다.
- **묶음 수정과 되돌리기**: 묶음에 사진을 넣고 빼는 기능(BestCut)과 결정 되돌리기(사진쏙, Favvy Undo)를 기본으로 넣는다. Favvy의 '관련 없는 사진까지 묶던 문제' 수정 사례를 보면 자동 묶기는 틀릴 수 있다.
- **'넣지 않을 사진' 자동 제외**: 스크린샷, 흔들린 사진, 영수증·서류 사진은 처음부터 후보에서 빼거나 접어 둔다(사진정리 한방).
- **얼굴·즐겨찾기 사진을 우선 후보로**: 정리 앱들이 '삭제 보호' 신호로 쓰는 얼굴·즐겨찾기를 뒤집어 '책에 넣을 우선 후보' 신호로 쓴다(사진정리 한방, 사진쏙). 기기 즐겨찾기를 읽어 오는 방식은 BestCut의 즐겨찾기 동기화를 참고한다.
- **아이별 필터와 단체사진 중복 소속**: 형제·쌍둥이 가정을 위해 아이별로 사진을 나누고, 함께 나온 사진은 양쪽에 모두 넣는다. 오분류는 사용자가 옮겨서 고치게 한다(키즈로그). 키즈로그는 서버에서 얼굴 임베딩을 처리하므로, 같은 방식을 쓰면 개인정보 고지·보관 정책이 필요하다.
- **결과를 '책에 담기' 목록으로 남기기**: 조사한 앱은 모두 삭제나 폴더 이동으로 끝난다. 포토북 편집기에서는 스와이프·버튼의 의미를 '삭제/유지'에서 '담기/제외'로 바꾸고, 결과를 선택 목록으로 저장해야 한다. 근거는 이 공백 자체다.
- **첫 로딩 대책**: 1년치를 처음에 한 번 분석하고 이후 새 사진만 증분 반영한다(사진정리 한방). 분석 중에는 남은 시간을 보여 준다(사진쏙).

**추론인 제안**
- 스와이프만 쓰면 1년치(수천 장)는 피로도가 크다. 그래서 '유사 묶음 접기 → 대표컷만 스와이프' 순서로 두 단계를 결합하는 편이 낫다(추론). Sponge 사용자가 유사 묶기를 계속 요청하는 점이 간접 근거다.
- 1:1 비교 화면(길게 눌러 전환)은 묶음 안에서 대표컷을 바꿀 때 보조 화면으로 두면 충분하다. 기본 흐름에 넣을 필요는 없다(추론).
- 월별 목표 장수(예: 페이지 수에 맞춘 월별 권장 장수)를 진행률과 함께 보여 주면 정리 앱의 '확보 용량' 지표를 포토북용 지표로 바꿀 수 있다(추론).
- 무료 사용 제한이나 잦은 결제 팝업은 선택 흐름을 끊는다(추론). 근거로 Favvy의 'PRO 팝업이 계속 뜬다', '무료 제한이 심하다'는 불만이 반복된다. 선택 단계 안에는 결제 장벽을 두지 않는 편이 낫다.

**주의**: AI 묶기·추천 앱 4개(BestCut, 사진쏙, 베스트컷, 사진정리 한방)는 다운로드 10~100+ 수준이고 리뷰가 없다. 추천 정확도는 검증되지 않았다(미확인). BestCut 업데이트 노트의 '베스트 샷 정확도 개선'도 정확도 문제가 있었다는 간접 정황일 뿐이다(미확인).

## 확인하지 못한 것

- BestCut: AI Photo Selection: 인앱 구매 상품의 종류와 가격
- BestCut: AI Photo Selection: 베스트 컷을 고르는 기준(선명도, 눈 감음, 표정 등)
- BestCut: AI Photo Selection: 실제 화면 흐름(그룹 목록과 비교 화면 구성) — 스크린샷을 보지 못함
- BestCut: AI Photo Selection: iOS 버전이 있는지 (App Store 검색 결과 없음)
- BestCut: AI Photo Selection: 인물·날짜별 분류나 필터 기능이 있는지
- BestCut: AI Photo Selection: 사용자 리뷰와 평점
- 사진쏙 - 중복·유사 사진 정리: iOS 버전이 있는지
- 사진쏙 - 중복·유사 사진 정리: 개인정보처리방침 원문 내용(JS로 렌더링되는 페이지라 읽지 못함)
- 사진쏙 - 중복·유사 사진 정리: 광고 SDK 종류와 광고 표시 위치
- 사진쏙 - 중복·유사 사진 정리: 실제 화면 흐름(스크린샷 미확인)과 날짜·기간 필터가 있는지
- 사진쏙 - 중복·유사 사진 정리: 인앱 결제나 유료 플랜이 있는지(토스페이먼츠 표기의 의미)
- 사진쏙 - 중복·유사 사진 정리: 베스트컷 판단 모델의 정확도와 사용자 평가
- 베스트컷 - 중복사진 정리 & 갤러리 용량 확보: 영문 앱 이름이 있는지
- 베스트컷 - 중복사진 정리 & 갤러리 용량 확보: 베스트컷을 자동으로 추천하는지(품질 점수 등), 아니면 순전히 사용자가 고르는지
- 베스트컷 - 중복사진 정리 & 갤러리 용량 확보: 광고 SDK가 실제로 데이터를 수집하는지와 개인정보처리방침 본문 내용
- 베스트컷 - 중복사진 정리 & 갤러리 용량 확보: iOS 버전이 있는지
- 베스트컷 - 중복사진 정리 & 갤러리 용량 확보: 실제 사용자 리뷰와 불만
- 사진정리 한방 - 중복 사진·동영상 한번에 삭제: 영문 앱 이름
- 사진정리 한방 - 중복 사진·동영상 한번에 삭제: 인앱결제가 일회성인지 구독인지, 상품 구성
- 사진정리 한방 - 중복 사진·동영상 한번에 삭제: 얼굴 검출이 단순 검출인지 인물 식별까지 하는지
- 사진정리 한방 - 중복 사진·동영상 한번에 삭제: 사용하는 온디바이스 모델·라이브러리
- 사진정리 한방 - 중복 사진·동영상 한번에 삭제: 실제 화면 흐름(스와이프 여부, 묶음 UI)
- 키즈로그 - 사진분류, 알림장, 보육일지: Google Play 인앱 상품 가격이 웹 표기 가격(4,900/9,900/19,900원)과 같은지
- 키즈로그 - 사진분류, 알림장, 보육일지: 분류 결과 화면에서 장 단위로 선택·삭제하거나 중복을 거를 수 있는지 (실제 UI 미확인)
- 키즈로그 - 사진분류, 알림장, 보육일지: 얼굴이 인식되지 않는 사진(뒷모습 등)을 어떻게 처리하는지
- 키즈로그 - 사진분류, 알림장, 보육일지: Google Play 평점과 리뷰 수 (페이지에 표시되지 않음)
- 키즈로그 - 사진분류, 알림장, 보육일지: 갤러리 폴더 저장이 Android와 iOS에서 같은 방식인지
- Sponge - Gallery Cleaner: Android Premium의 정확한 가격 구성(구독/평생)과 한국 가격
- Sponge - Gallery Cleaner: Play 스토어 순위
- Sponge - Gallery Cleaner: 폴더 이동 기능의 상세 화면 흐름(목적 폴더 선택 방식)
- Sponge - Gallery Cleaner: 부정 리뷰에서 반복되는 불만(버그, 결제 등)
- Favvy: Clean your photos: Android 원화(KRW) 구독 가격과 무료판의 하루 스와이프 한도 수치
- Favvy: Clean your photos: 흐린 사진·어두운 사진·저화질 사진을 앱이 실제로 자동 감지해 따로 모아 주는지, 아니면 설명 문구일 뿐인지
- Favvy: Clean your photos: 오른쪽 스와이프(남기기)한 사진을 별도 앨범이나 즐겨찾기로 표시해 주는지
- Favvy: Clean your photos: 중복·유사 사진 묶음에 AI를 쓰는지 해시 같은 규칙을 쓰는지, 묶음 안에서 대표 사진을 추천하는지
- Favvy: Clean your photos: iOS 스토어의 'Contains Advertising' 표시와 자사 'No ads, ever' 주장 중 어느 쪽이 맞는지

## 부록: 대상별 상세

### BestCut: AI Photo Selection

- **앱 정체** ✓: BestCut: AI Photo Selection (국문 스토어 페이지에서도 영문 이름을 그대로 씀). Google Play: https://play.google.com/store/apps/details?id=com.basicworld.BestCut . 개인정보처리방침의 앱 이름도 'BestCut'으로, 패키지 ID·개발자 연락처(basicworld.maker@gmail.com)가 서로 맞아 같은 이름의 다른 앱과 섞이지 않았다고 판단했다. 카테고리는 '사진', 마지막 업데이트는 2025-09-27이다. [1](https://play.google.com/store/apps/details?id=com.basicworld.BestCut&hl=ko&gl=KR) [2](https://sites.google.com/view/bestcut-privacy/%ED%99%88)
- **개발사·국가** ✓: 개발자 표기는 basicworld(개인 개발자로 보임)이다. Play 개발자 정보의 이름은 '구기본', 주소는 경상남도 창원시 의창구 감계로 342, 국가는 대한민국(South Korea)이다. 법인 이름은 확인하지 못했다. _(법인인지는 미확인. Play에 적힌 연락처를 보면 개인 개발자일 가능성이 높다)_ [1](https://play.google.com/store/apps/details?id=com.basicworld.BestCut&hl=ko&gl=KR)
- **플랫폼**: Android(Google Play)는 확인했다. iOS App Store 검색(itunes search API)에서는 결과가 나오지 않았고, 웹 버전도 없다. 개발자 블로그(basicworldhome.blogspot.com)에는 글이 없다. [1](https://play.google.com/store/apps/details?id=com.basicworld.BestCut&hl=ko&gl=KR) [2](https://basicworldhome.blogspot.com)
- **핵심 기능**: 1) AI 스캔: 비슷한 시간대·각도로 찍힌 사진을 자동으로 묶는다. 2) 베스트 샷 추천: 묶음마다 가장 잘 나온 한 장('베스트 컷')을 추천한다. 3) 수동 편집: 탭 한 번으로 묶음에 사진을 넣거나 뺀다. 4) 즐겨찾기 동기화: 앱에서 '좋아요'한 사진이 기기 기본 갤러리 즐겨찾기에도 등록된다. 5) 안전 삭제: 지운 사진은 영구 삭제되지 않고 시스템 휴지통으로 간다. 6) 빠른 검색(Quick Search): 업데이트 노트에만 이름이 나온다. _(스토어 설명(자사 출처) 기준. 실제로 써 보지는 않았다)_ [1](https://play.google.com/store/apps/details?id=com.basicworld.BestCut&hl=ko&gl=KR)
- **관점 관련 기능** ✓: 스토어 설명으로 짐작한 흐름은 다음과 같다. 갤러리를 AI로 스캔하면, 비슷한 시간·각도의 연속 촬영 사진이 그룹으로 묶여 목록에 나온다. 그룹마다 AI가 베스트 컷 한 장을 추천한다. 사용자는 추천을 받아들이거나, 그룹 구성이 틀렸으면 탭으로 사진을 넣고 뺀다. 남길 사진은 '좋아요'를 누르고(기본 갤러리 즐겨찾기와 동기화), 나머지는 골라서 시스템 휴지통으로 보낸다. 묶기와 추천은 자동이고, 남길 사진과 지울 사진은 사용자가 확정한다. 연간 포토북 선별에 바로 참고할 수 있는 패턴은 세 가지다. ① 시간·각도 기준으로 비슷한 사진 묶기 ② 묶음당 대표 1장 추천 ③ '좋아요'를 OS 즐겨찾기와 양방향으로 쓰기. 인물·아이 인식, 날짜·이벤트별 분류, 스와이프 선별, 필터 기능은 설명에 없다. 베스트 컷을 어떤 기준(흔들림, 눈 감음, 표정 등)으로 고르는지도 공개돼 있지 않다. _(자사 출처(스토어 설명)만 확인했고 화면 스크린샷은 보지 못했다. 정리 앱이라 '삭제'에 초점이 있고, 책에 넣을 사진을 고르는 용도는 아니다)_ [1](https://play.google.com/store/apps/details?id=com.basicworld.BestCut&hl=ko&gl=KR)
- **AI 사용·처리 방식**: 비슷한 사진 묶기와 베스트 샷 추천에 AI를 쓴다. 개인정보처리방침에 따르면 모든 사진 분석·처리는 기기 안에서만 이뤄지고 외부 서버로 보내지 않는다(온디바이스). 어떤 모델이나 기술을 쓰는지는 미확인이다. _(자사 출처(개인정보처리방침))_ [1](https://sites.google.com/view/bestcut-privacy/%ED%99%88) [2](https://play.google.com/store/apps/details?id=com.basicworld.BestCut&hl=ko&gl=KR)
- **가격 모델** ✓: 무료이고 광고가 들어간다(Google AdMob). Play에 '앱에서 바로 구매(인앱 구매)'가 표시되지만, 상품 종류와 가격은 페이지에 나오지 않아 미확인이다. [1](https://play.google.com/store/apps/details?id=com.basicworld.BestCut&hl=ko&gl=KR) [2](https://sites.google.com/view/bestcut-privacy/%ED%99%88)
- **평점·규모** ✓: Google Play 다운로드 100회 이상(100+). 평점과 리뷰 수는 페이지에 나오지 않는다(평가가 너무 적어 표시가 안 되는 것으로 보임). 순위권 밖의 아주 작은 앱이다. [1](https://play.google.com/store/apps/details?id=com.basicworld.BestCut&hl=ko&gl=KR)
- **개인정보 처리**: 방침상 사진·영상은 기기 안에서만 분석하고 외부 서버로 보내거나 저장하지 않는다. 광고용 Google AdMob이 기기 정보, IP, 광고 ID(ADID)를 수집할 수 있다. Play 데이터 보안 항목에는 '수집된 데이터 없음', '앱 활동·기기 또는 기타 ID를 제3자와 공유할 수 있음', '전송 중 데이터 암호화'라고 적혀 있다. 개인정보처리방침 시행일은 2025-09-18이다. _(자사 출처(방침·개발자 신고 내용))_ [1](https://sites.google.com/view/bestcut-privacy/%ED%99%88) [2](https://play.google.com/store/apps/details?id=com.basicworld.BestCut&hl=ko&gl=KR)
- **주요 불만**: 미확인. 공개 리뷰나 커뮤니티 언급을 찾지 못했다. 업데이트 노트에 '빠른 검색 오류 수정', '삭제 실패 오류 수정', '베스트 샷 정확도 개선'이 있어, 삭제 오류와 추천 정확도 문제가 있었던 것으로 보인다. [1](https://play.google.com/store/apps/details?id=com.basicworld.BestCut&hl=ko&gl=KR)
- **기타**: 한국 개인 개발자가 만든 아주 작은 앱이다(다운로드 100+, 2025-09 출시로 추정). 시장 참고 사례로서의 무게는 작다. 다만 '비슷한 사진 그룹 → 대표 1장 추천 → 사용자가 확정 → OS 즐겨찾기와 동기화'라는 흐름은 연간 포토북 사진 선택 화면을 설계할 때 바로 참고할 수 있다. 같은 순간 연속 촬영 사진을 1장으로 줄이는 단계에 해당한다. 개발자 블로그(basicworldhome.blogspot.com)에는 글이 없다.

### 사진쏙 - 중복·유사 사진 정리

- **앱 정체** ✓: 사진쏙 - 중복·유사 사진 정리. 영문명은 스토어에 따로 표기되지 않았고, 패키지 ID(com.snappick.app)와 개인정보처리방침 도메인(snap-pick.bethany.ai.kr)으로 보아 내부 명칭은 'SnapPick'으로 보인다. 스토어 링크: https://play.google.com/store/apps/details?id=com.snappick.app . 스토어 짧은 소개: 'AI가 비슷한 사진을 묶고 베스트컷만 남겨요. 중복·흐린 사진 정리로 저장공간 확보'. _(영문명 SnapPick은 패키지·도메인에서 추정한 것이다)_ [1](https://play.google.com/store/apps/details?id=com.snappick.app&hl=ko&gl=KR)
- **개발사·국가** ✓: 스토어 개발자 계정은 BoazHwang이다. 개발자 소개에는 '마중물'로 나오며 주소는 대한민국 경기도 성남시 분당구 벌말로30번길 46, 706호(야탑동)이다. 통신판매업 신고 번호(2024-경기광주-0647)로 보아 개인사업자로 추정된다. 국가는 대한민국. _(법인인지 개인사업자인지는 스토어 정보만으로 판단했다)_ [1](https://play.google.com/store/apps/details?id=com.snappick.app&hl=ko&gl=KR)
- **플랫폼**: Android(Google Play)는 확인했다. iOS 버전과 웹 버전은 확인하지 못했다(웹 검색과 App Store 검색 결과에 나오지 않음). [1](https://play.google.com/store/apps/details?id=com.snappick.app&hl=ko&gl=KR)
- **핵심 기능**: 1) 중복·유사 사진 자동 그룹화(연사, 같은 장면 반복 촬영) 2) 그룹마다 베스트컷 추천(선명도, 눈 뜬 표정, 미소 기준) 3) 흐린 사진과 눈 감은 사진을 정리 후보로 따로 표시 4) '오늘의 사진 정리'로 당일 촬영분 중 정리할 사진 제안 5) 추천에서 빠진 사진 일괄 삭제(기기 휴지통으로 이동, 30일 안에 복구 가능) _(개발자가 직접 쓴 스토어 설명(자사 출처)이다)_ [1](https://play.google.com/store/apps/details?id=com.snappick.app&hl=ko&gl=KR)
- **관점 관련 기능** ✓: 흐름은 '사진 접근 허용 → 전체 스캔(남은 시간 표시) → 유사 사진 그룹 목록과 그룹별 베스트컷 표시 → 사용자가 확인하고 정리'이다. v1.3부터 홈 화면이 사진 중심으로 바뀌어 베스트 샷을 크게 보고 바로 판단할 수 있다. 그룹 검토 화면에는 '보관/정리' 버튼이 있어 한 장씩 빠르게 결정하는 이진 선별 방식이고, 정리 목록에서 뺀 사진은 되돌리기로 바로 복구된다. 자동화 수준은 '그룹화와 베스트컷 후보까지 자동, 최종 결정은 사용자'이며 스토어 설명에 '어떤 사진을 지울지는 항상 직접 확인하고 결정'한다고 적혀 있다. 베스트컷 판단 기준은 선명도, 눈 뜬 표정, 미소이고, 흐린 사진과 눈 감은 사진은 별도 후보로 표시된다. 안전장치로 즐겨찾기, 인물 사진, 최근 사진, 클라우드에만 있는 사진이 삭제 대상에 들어 있으면 먼저 경고한다. 즉 즐겨찾기와 인물 여부를 신호로 읽는다. 다만 목적이 '남길 사진 고르기'가 아니라 '지울 사진 고르기(용량 확보)'이고, 아이 인식, 인물별 분류, 기간·연도 필터, 앨범 만들기는 확인되지 않았다. 연간 포토북 선택 단계에 참고할 만한 패턴은 '유사 그룹 → 대표 1장 자동 추천 → 보관/정리 이진 결정 → 되돌리기'이다. _(자사 출처(스토어 설명과 업데이트 노트)만으로 정리했고 실제 화면은 확인하지 못했다)_ [1](https://play.google.com/store/apps/details?id=com.snappick.app&hl=ko&gl=KR)
- **AI 사용·처리 방식**: AI로 유사·중복 사진을 묶고 베스트컷을 고른다(선명도, 눈 뜬 표정, 미소 판단). 흐린 사진과 눈 감은 사진도 탐지한다. 스토어 설명에 따르면 사진 분석은 모두 휴대폰 안에서 이루어지는 온디바이스 방식이고, 사진을 서버에 올리지 않는다. 어떤 모델이나 프레임워크를 쓰는지는 미확인. _(자사 출처)_ [1](https://play.google.com/store/apps/details?id=com.snappick.app&hl=ko&gl=KR)
- **가격 모델** ✓: 무료이며 '광고 포함'으로 표시된다. 스토어 페이지에 인앱 구매 표기는 없었다. 다만 개발자 정보에 토스페이먼츠가 함께 적혀 있어 앞으로 결제 기능이 생길 가능성은 있다(미확인). [1](https://play.google.com/store/apps/details?id=com.snappick.app&hl=ko&gl=KR)
- **평점·규모** ✓: Google Play 다운로드는 '10회 이상'이다. 평점과 리뷰 수는 표시되지 않아 리뷰가 없거나 거의 없는 것으로 보이며, 순위 정보도 없다. 최근 업데이트는 2026-10-17(v1.3). [1](https://play.google.com/store/apps/details?id=com.snappick.app&hl=ko&gl=KR)
- **개인정보 처리**: Google Play 데이터 보안 항목 기준으로 제3자와 공유하는 데이터는 없다. 수집 항목은 이메일 주소와 사용자 ID(선택사항, 계정 관리용), 비정상 종료 로그와 성능 데이터(분석용), 앱 상호작용(분석용), 기기 ID(분석용)이다. 전송 중 데이터는 암호화되고 데이터 삭제를 요청할 수 있다. 사진은 기기 안에서만 분석하고 업로드하지 않는다고 설명한다. 다만 광고가 포함되어 있어 광고 SDK가 어떤 데이터를 쓰는지는 데이터 보안 항목과 함께 볼 필요가 있다. 개인정보처리방침(snap-pick.bethany.ai.kr/privacy)은 JS로 렌더링되는 페이지라 읽지 못했다. _(개발자 자기 신고 기준)_ [1](https://play.google.com/store/apps/datasafety?id=com.snappick.app&hl=ko) [2](https://play.google.com/store/apps/details?id=com.snappick.app&hl=ko&gl=KR)
- **주요 불만**: 미확인. 스토어 리뷰가 없고 커뮤니티 언급도 검색되지 않았다. [1](https://play.google.com/store/apps/details?id=com.snappick.app&hl=ko&gl=KR)
- **기타**: 다운로드가 10회 이상 수준인 아주 작은 1인(개인사업자 추정) 앱이라 시장 영향력은 없다. 그래도 v1.3에서 바꾼 UX는 연간 포토북 사진 선택 화면에 참고할 만하다: 베스트샷을 크게 보여 주고, 그룹 단위로 보관/정리 버튼을 눌러 이진 결정하고, 정리 목록에서 뺀 사진은 되돌리기로 바로 복구한다. 삭제 전에 즐겨찾기·인물·최근·클라우드 전용 사진이 들어 있으면 경고하는 장치도 있는데, 이 신호들은 포토북 사진 선택 우선순위의 근거로 바꿔 쓸 수 있다.

### 베스트컷 - 중복사진 정리 & 갤러리 용량 확보

- **앱 정체** ✓: 베스트컷 - 중복사진 정리 & 갤러리 용량 확보 (영문 이름 미확인). Google Play: https://play.google.com/store/apps/details?id=com.poty0808.photo_compare . 카테고리는 '도구', 최근 업데이트 2026-11-09. 패키지 ID와 개발자 표기 'poty.'가 일치하는 것을 근거로 특정함. '베스트컷'이라는 이름이 붙은 다른 사진 앱과 혼동하지 않았다. [1](https://play.google.com/store/apps/details?id=com.poty0808.photo_compare&hl=ko&gl=KR)
- **개발사·국가** ✓: 개발자 표기는 'poty.'이고, 개발자 소개에는 개인 이름 '이종언'과 South Korea가 나온다. 법인이 아닌 한국 개인 개발자로 보인다. 찬송가, 가계부, 수면 등 다른 소형 앱도 여러 개 운영한다. _(법인명은 확인되지 않음. 개인 개발자로 추정)_ [1](https://play.google.com/store/apps/details?id=com.poty0808.photo_compare&hl=ko&gl=KR)
- **플랫폼**: Android(Google Play)만 확인됨. iOS 버전과 웹 버전은 찾지 못함(App Store 관련 검색에도 나오지 않음). [1](https://play.google.com/store/apps/details?id=com.poty0808.photo_compare&hl=ko&gl=KR)
- **핵심 기능**: 1) 한장씩 비교 모드: 두 장을 나란히 놓고 고르면 나머지는 삭제. 2) 여러장 비교 모드: 비슷한 사진을 그룹으로 묶어 한 화면에 보여주고, 남길 사진을 탭하면 나머지는 일괄 삭제. 3) 완전 중복 삭제: SHA-256으로 바이트까지 같은 파일을 찾아 삭제. 4) 날짜 범위를 골라 그 기간만 스캔. 5) Android 시스템 팝업으로 일괄 삭제하고 휴지통에서 복구 가능(Android 11 이상). _(스토어 설명문(자사 출처) 기준)_ [1](https://play.google.com/store/apps/details?id=com.poty0808.photo_compare&hl=ko&gl=KR)
- **관점 관련 기능** ✎: The app has three modes. (1) 한장씩 비교: two photos side by side; holding the compare button switches between them instantly, and the photos you do not pick are deleted. (2) 여러장 비교: similar photos are grouped on one screen; tap the ones to keep and the rest are deleted together (aimed at burst and landscape shots). (3) 완전 중복 삭제: SHA-256 finds files that are 100% identical, such as copies saved from KakaoTalk or Instagram, and removes them all after one confirmation. Grouping: photos within 50m by GPS are compared first; photos without GPS are grouped by capture time within 2 minutes; perceptual hashing then judges visual similarity, tolerating small changes in brightness or color. A date range can limit the scan; with no date set, the whole gallery is scanned. Deletion goes through a confirmation step and one Android system popup, and deleted photos can be recovered from the Android trash on Android 11 and later. The description mentions no automatic best-shot scoring, no person or child recognition, and no favorites, filters, swipe selection, or export or collection of the chosen photos. _(스토어 설명문(자사 출처)만으로 확인했고, 실제 앱을 사용해 보지는 않았음 [검증에서 수정: 원래 값 "유사 사진 묶기: 50m 안의 같은 장소(GPS)에서 찍은 사진끼리 먼저 비교한다. GPS가 없으면 촬영 시간이 2분 안인 사진끼리 후보로 묶는다. 그다음 지각적 해시(Perceptual Hash)로 시각적 유사도를 판단하므로 밝기나 색이 조금 달라도 같은 그룹으로 잡는다. 사진을 고르는 흐름은 두 가지다. (a) 한장씩 비교: 두 장을 나란히 띄우고, 비교 버튼을 꾹 누르면 다른 사진으로 즉시 바뀌어 차이를 빠르게 볼 수 있다. 마음에 드는 쪽을 고르면 나머지는 삭제 대상이 된다. (b) 여러장 비교: 그룹 전체를 한 화면에 보여주고, 남길 사진을 탭하면 나머지가 한 번에 삭제된다. 기간을 지정해 그 범위만 스캔할 수도 있다(예: 1년, 특정 행사). 정리하면 사람이 남길 컷을 직접 고르는 반자동 방식이다. 앱이 베스트컷을 자동으로 추천하는지(화질·초점·표정 점수 등)는 설명에 없다. 인물이나 아이 인식, 얼굴별 분류, 즐겨찾기, 필터, 스와이프 선별 기능도 설명에 나오지 않는다. 고른 결과는 '나머지 삭제'로 끝나며, 선택한 사진을 따로 모으거나 내보내는 기능은 확인되지 않았다."])_ [1](https://play.google.com/store/apps/details?id=com.poty0808.photo_compare&hl=ko&gl=KR) [2](https://play.google.com/store/apps/details?id=com.poty0808.photo_compare&hl=ko&gl=KR)
- **AI 사용·처리 방식**: 설명에 AI나 머신러닝이라는 표현은 없다. 지각적 해시와 SHA-256 같은 알고리즘, GPS·시간 메타데이터로 비교한다. Play 데이터 보안 항목에 '수집된 데이터 없음'으로 되어 있어 온디바이스에서 처리하는 것으로 추정되지만, 직접 확인하지는 못했다. [1](https://play.google.com/store/apps/details?id=com.poty0808.photo_compare&hl=ko&gl=KR)
- **가격 모델** ✓: 무료이며 '광고 포함' 표시가 있다. Play 페이지에 '인앱 구매' 표시는 없다. [1](https://play.google.com/store/apps/details?id=com.poty0808.photo_compare&hl=ko&gl=KR)
- **평점·규모** ✓: Google Play 다운로드 10회 이상(10+). 평점과 평가 수는 표시되지 않아 평가가 부족한 것으로 보인다. 순위 정보는 없다. _(Google Play 표시값, 2026-11-25 기준)_ [1](https://play.google.com/store/apps/details?id=com.poty0808.photo_compare&hl=ko&gl=KR)
- **개인정보 처리**: Play 데이터 보안 항목에는 개발자 자기 신고 기준으로 '제3자와 공유되는 데이터 없음'과 '수집된 데이터가 없습니다'로 되어 있다. 다만 광고가 들어 있으므로 광고 SDK가 실제로 데이터를 수집하는지는 확인하지 못했다. 개인정보처리방침 링크는 있으나 본문은 읽지 않았다. _(개발자가 직접 신고한 정보)_ [1](https://play.google.com/store/apps/details?id=com.poty0808.photo_compare&hl=ko&gl=KR)
- **주요 불만**: 미확인. 평가와 리뷰가 거의 없고(다운로드 10+), 커뮤니티에서 언급된 것도 찾지 못했다. [1](https://play.google.com/store/apps/details?id=com.poty0808.photo_compare&hl=ko&gl=KR)
- **기타**: 이 앱의 '그룹 묶기 규칙'은 연간 포토북 편집기에서 사진을 고르는 단계에 그대로 참고할 만하다. 규칙은 GPS 50m 이내, 또는 촬영 시간 2분 이내인 사진을 먼저 후보로 모은 뒤 지각적 해시로 확정한다. 컷을 고르는 화면은 1:1 비교(버튼을 길게 누르면 다른 사진으로 전환)와 그룹 그리드(남길 사진 탭) 두 가지다. 날짜 범위로 스캔 대상도 줄일 수 있다. 다만 결과가 '삭제'로 끝나므로, 포토북에 맞추려면 '삭제' 대신 '책에 담기/제외'로 바꿔야 한다. 출시 초기의 소규모 개인 앱이라(다운로드 10+) 시장에서 검증된 사례는 아니다.

### 사진정리 한방 - 중복 사진·동영상 한번에 삭제

- **앱 정체** ✓: 사진정리 한방 - 중복 사진·동영상 한번에 삭제 (영문명 미확인. 개인정보처리방침 URL 슬러그가 'photo-cleaner-privacy'). Google Play: https://play.google.com/store/apps/details?id=kr.photo.hanbang . 패키지 ID, 개발자 표시명 hoi79, 김포 주소가 모두 식별 정보와 일치한다. [1](https://play.google.com/store/apps/details?id=kr.photo.hanbang&hl=ko&gl=KR)
- **개발사·국가** ✓: 개인 개발자 이정호(Play 표시명 hoi79). 대한민국 경기도 김포시. 페이지에 사업자번호 206-27-47779와 통신판매업 신고번호 2026-경기김포-4886(김포시청)이 적혀 있다. 법인은 아니며 개인사업자로 보인다. _(법인이 아닌 개인(사업자) 명의)_ [1](https://play.google.com/store/apps/details?id=kr.photo.hanbang&hl=ko&gl=KR)
- **플랫폼**: Android(Google Play)만 확인됐다. iOS판과 웹판은 찾지 못했다. [1](https://play.google.com/store/apps/details?id=kr.photo.hanbang&hl=ko&gl=KR)
- **핵심 기능**: 1) 중복 사진: 같은 사진 여러 장 중 남길 1장을 골라 보여 준다. 2) 연사·유사 사진: 비슷한 사진을 묶고 가장 선명한 한 장을 추천한다. 3) 스크린샷: 저장 경로로 구분해 모아 준다. 4) 흔들린 사진: 초점이 흐린 사진을 골라낸다. 5) 영수증·서류: 글자가 많은 사진을 따로 모은다. 6) 대용량 동영상: 큰 동영상을 크기순으로 보여 주고, 지우기 전에 늘어날 용량을 먼저 보여 준다. _(스토어 설명(자사 출처) 기준)_ [1](https://play.google.com/store/apps/details?id=kr.photo.hanbang&hl=ko&gl=KR)
- **관점 관련 기능** ✓: 이 앱은 '지울 사진 고르기'에 맞춰져 있다. 남길 사진을 고르는 연간 포토북과는 방향이 반대다. 흐름은 다음과 같다. 처음 한 번 전체를 분석하고, 그 뒤에는 새로 찍은 사진만 반영한다. 분석 결과는 중복, 연사, 스크린샷, 흔들림, 영수증·서류, 대용량 동영상 카테고리로 자동 분류된다. 중복 묶음에서는 남길 1장을, 연사 묶음에서는 '가장 선명한 한 장'을 추천한다. 즉 선명도를 기준으로 베스트컷을 고른다. 사용자는 목록을 눈으로 확인하고 체크한 사진만 삭제한다. 보호 장치가 있다. 얼굴이 나온 사진은 정리 대상에서 빠지고(얼굴 검출로 보이나 개인 식별 여부는 미확인), 갤러리 즐겨찾기(하트) 사진도 건드리지 않는다. 포토북 기획 관점에서 쓸 만한 점은 세 가지다. 유사컷 묶음과 선명도 기반 대표컷 추천, 흔들림·스크린샷·서류 같은 '책에 넣지 않을 사진' 자동 제외, 얼굴·즐겨찾기를 신호로 쓰는 방식. 반면 아이별 인물 분류, 날짜·이벤트별 정리, 스와이프 선별 UI는 설명에 없다. _(자사 스토어 설명 기준이며 실제 화면은 확인하지 못했다)_ [1](https://play.google.com/store/apps/details?id=kr.photo.hanbang&hl=ko&gl=KR)
- **AI 사용·처리 방식**: 분석과 분류는 모두 기기 안에서만 처리한다고 밝힌다('사진은 폰 안에서만 분석', 개인정보처리방침 '100% 온디바이스'). 쓰이는 곳은 중복·유사 판정, 선명도·흔들림 판정, 얼굴 검출, 글자 많은 사진 판별이다. 어떤 모델이나 라이브러리를 쓰는지(예: ML Kit)는 확인하지 못했다. _(자사 출처)_ [1](https://play.google.com/store/apps/details?id=kr.photo.hanbang&hl=ko&gl=KR) [2](https://sites.google.com/view/photo-cleaner-privacy)
- **가격 모델** ✓: 무료이며 광고와 인앱결제가 있다. 500MB까지는 무료로 비울 수 있고, 그 뒤로는 15초 광고를 보면 1GB씩 더 비울 수 있다. 인앱 상품 가격은 ₩2,500~₩3,900이다. 개인정보처리방침에 따르면 인앱결제는 광고 제거 상품이다. 일회성인지 구독인지는 확인하지 못했다. [1](https://play.google.com/store/apps/details?id=kr.photo.hanbang&hl=ko&gl=KR) [2](https://sites.google.com/view/photo-cleaner-privacy)
- **평점·규모** ✓: Google Play 다운로드는 10회 이상이다. 평점과 리뷰는 아직 표시되지 않는다. 출시가 2026-11-24이므로 규모라고 할 만한 수치가 없다. 순위 정보도 없다. [1](https://play.google.com/store/apps/details?id=kr.photo.hanbang&hl=ko&gl=KR)
- **개인정보 처리**: Play 데이터 보안 항목에는 '수집 데이터 없음', '제3자 공유 없음'으로 선언돼 있다. 개인정보처리방침(시행 2026-11-08)에 따르면 미디어는 외부 서버로 전송하지 않고, 권한은 READ_MEDIA_IMAGES와 READ_MEDIA_VIDEO를 쓴다. 다만 광고용으로 Google AdMob이 광고 ID를 쓸 수 있다고 적혀 있다. 결제는 Google Play Billing으로 처리한다. _(AdMob이 광고 ID를 쓰는데도 '수집 없음'으로 선언한 점은 서로 맞지 않는다)_ [1](https://play.google.com/store/apps/details?id=kr.photo.hanbang&hl=ko&gl=KR) [2](https://sites.google.com/view/photo-cleaner-privacy)
- **주요 불만**: 미확인. 출시 직후라 리뷰가 없고, 커뮤니티 언급도 검색되지 않았다. [1](https://play.google.com/store/apps/details?id=kr.photo.hanbang&hl=ko&gl=KR)
- **기타**: '얼굴이 나온 사진은 삭제 대상에서 자동 제외'하는 설계는 포토북 선택 단계에 그대로 뒤집어 쓸 수 있다. 얼굴이 있는 사진을 기본 후보로 두고, 흔들림·스크린샷·서류는 후보에서 빼는 식이다. 연사 묶음에서 '가장 선명한 1장'을 추천하는 방식도 유사컷 대표 선택 UX로 참고할 만하다. 또 '한 번 분석 후 새 사진만 증분 반영'하는 구조는 1년치 사진을 다루는 편집기의 첫 로딩 시간 문제와 직결된다. 다만 출시 하루 된 개인 개발 앱이라 실제 품질은 검증되지 않았다.

### 키즈로그 - 사진분류, 알림장, 보육일지

- **앱 정체** ✓: 키즈로그 - 사진분류, 알림장, 보육일지 (영문 서비스명 KidsLog). Google Play: https://play.google.com/store/apps/details?id=com.hunjun.kidslog / App Store: https://apps.apple.com/kr/app/id6778382653 (iPhone 전용). 어린이집·유치원 교사가 반 사진을 아이별로 분류하고 알림장·보육일지를 AI로 쓰는 업무용 앱이다. 부모용 성장 앨범 앱이 아니다. 키즈노트(카카오 원-가정 소통 앱)와는 별개이고, 만든 알림장을 복사해 키즈노트에 붙여넣는 보조 도구로 포지셔닝한다. _(웹사이트는 자사 출처)_ [1](https://play.google.com/store/apps/details?id=com.hunjun.kidslog&hl=ko&gl=KR) [2](https://apps.apple.com/kr/app/id6778382653) [3](https://kidslog-web.vercel.app)
- **개발사·국가** ✓: 셀리(개인사업자, 대표 이현준), 대한민국(전라남도 목포 소재, 사업자등록번호 435-41-01455). Google Play의 개발자 표기는 '셀리 / 이현준 / South Korea'이고, App Store 판매자 표기는 'HYUNJUN LEE'다. 법인이 아니라 개인 운영 서비스로 보인다. _(약관은 자사 출처. 스토어 표기와 서로 일치한다.)_ [1](https://kidslog-web.vercel.app/terms) [2](https://play.google.com/store/apps/details?id=com.hunjun.kidslog&hl=ko&gl=KR) [3](https://apps.apple.com/kr/app/id6778382653)
- **플랫폼**: Android(Google Play)와 iOS(iPhone 전용, 2026-06-25 출시)를 지원한다. 웹(kidslog-web.vercel.app)에 로그인하면 앱에서 만든 기록을 PC에서 보고 복사하거나 구독을 관리할 수 있다. 사진 업로드와 알림장 생성은 앱에서만 된다. [1](https://kidslog-web.vercel.app) [2](https://apps.apple.com/kr/app/id6778382653)
- **핵심 기능**: 1) 얼굴 인식으로 원아별 사진 자동 분류 후 휴대폰 갤러리에 아이별 폴더로 저장 2) 사진이나 짧은 메모로 AI 알림장 생성(반 전체 일괄 생성 가능) 3) 알림장을 바탕으로 학급 보육일지 작성(2024 개정 평가지표 7섹션형 또는 간편형) 4) 관찰일지·발달평가서·적응일지·상담일지 초안 작성 5) 놀이계획(월간 보육계획안, 주제별 놀이 찾기) 6) 낮잠 음악, 지난 날짜 기록 작성 _(자사 설명 기반)_ [1](https://play.google.com/store/apps/details?id=com.hunjun.kidslog&hl=ko&gl=KR) [2](https://kidslog-web.vercel.app)
- **관점 관련 기능** ✓: 사진 정리 기능은 '인물(아이)별 자동 분류' 하나에 집중돼 있다. 흐름은 다음과 같다. (1) 처음에 반 아이 이름을 등록한다. 웹사이트는 '처음 한 번만 이름을 등록하면 다음부터는 자동'이라고 설명한다. (2) 그날 찍은 반 사진을 골라 올린다. 한 번에 최대 100장까지 올릴 수 있다. (3) 서버가 얼굴을 인식해 아이별로 나눈다. 예시 화면에는 '사진 33장 분류 완료 → 민준 12장/서아 9장/지유 7장/단체사진 5장'처럼 아이별 장수와 단체사진 묶음이 나온다. (4) 단체사진은 함께 나온 아이 모두에게 들어간다. (5) 분류 결과는 휴대폰 갤러리에 아이별 앨범(폴더)으로 저장된다. 교사는 이후 키즈노트에서 사진을 첨부할 때 그 앨범을 고른다. (6) 오분류는 사용자가 사진을 다른 아이로 옮겨 고친다(사진 분리). 이렇게 옮기면 다음부터 따로 인식된다. 쌍둥이·형제자매가 한 아이로 묶인 경우가 대표 사례다. (7) 분류된 아이별 사진은 그대로 알림장 생성 입력으로 이어진다. 유사·중복 묶기, 베스트컷 추천, 즐겨찾기·필터, 스와이프 선별 같은 기능은 공식 설명에서 확인되지 않는다. 사진 원본은 알림장을 만들면 삭제되고, 만들지 않아도 업로드 24시간 후 삭제되므로 앱 안에 장기 앨범이 남지 않는다. 장기 보관은 기기 갤러리의 아이별 폴더가 맡는다. 연간 포토북 관점에서는 '대량 업로드 → 인물별 자동 버킷팅 → 단체사진 다중 소속 → 수동 이동으로 재학습'이라는 패턴을 참고할 수 있다. _(자사 홈페이지·스토어 설명 기반이며 실제 화면은 직접 확인하지 않았다. 베스트컷 추천이나 중복 묶기가 없다는 결론은 공식 설명에 언급이 없다는 근거뿐이다.)_ [1](https://kidslog-web.vercel.app) [2](https://play.google.com/store/apps/details?id=com.hunjun.kidslog&hl=ko&gl=KR) [3](https://apps.apple.com/kr/app/id6778382653)
- **AI 사용·처리 방식**: 두 곳에 AI를 쓴다. (1) 얼굴 인식·분류: 운영사가 직접 운영하는 자체 서버에서 오픈소스 InsightFace로 처리한다. 클라우드(자체 서버) 방식이며 온디바이스가 아니다. 얼굴 영역 좌표와 512차원 임베딩 벡터를 저장해 새 사진을 재처리 없이 분류한다. (2) 알림장·보육일지·관찰기록 생성: 원아 사진·이름·나이·활동 내용을 Anthropic PBC(미국) API로 보내 생성한다. 약관에는 'Anthropic Claude'로 명시돼 있다. 교사 검토가 필수인 초안으로 안내한다. _(자사 개인정보처리방침 기준)_ [1](https://kidslog-web.vercel.app/privacy) [2](https://kidslog-web.vercel.app/terms)
- **가격 모델** ✓: 앱은 무료로 설치하고 구독으로 이용한다. Light 월 4,900원(텍스트 알림장 월 100건), Basic 월 9,900원(사진·텍스트 알림장 월 200건), Pro 월 19,900원(월 400건)이다. AI 사진 자동 분류는 모든 플랜에서 무제한이다. 연간 결제 시 2개월이 무료(약 17% 할인)다. 무료 체험은 알림장 생성 3회(앱 버전 1.0.3 노트)이며, 추천 코드를 입력하면 10회가 지급된다. 결제 후 7일 이내이고 사용하지 않았으면 환불된다. _(웹사이트 표기 가격(자사 출처)이다. 스토어 인앱 가격은 직접 확인하지 못했다. 웹 결제는 카카오페이 정기결제이고, iOS는 Apple ID로 청구된다.)_ [1](https://kidslog-web.vercel.app) [2](https://apps.apple.com/kr/app/id6778382653) [3](https://kidslog-web.vercel.app/terms)
- **평점·규모** ✓: Google Play 다운로드 1천+ 회이며, 평점은 페이지에 표시되지 않는다(평가 수 부족으로 추정). App Store는 평점 5.0, 평가 4개(iTunes lookup 기준)다. 2026-06-25 출시된 신생 앱이고 최신 버전은 1.0.8(2026-09-19)이다. 순위와 가입자 수 정보는 없다. [1](https://play.google.com/store/apps/details?id=com.hunjun.kidslog&hl=ko&gl=KR) [2](https://itunes.apple.com/lookup?id=6778382653&country=kr)
- **개인정보 처리**: 데이터 저장 및 인증은 Supabase Inc.에 위탁한다. 원아 사진 원본은 알림장을 생성하면 삭제되고, 생성하지 않아도 업로드 24시간 후 자동 삭제된다(2026-10-31 개정, 이전 7일). 단체사진은 함께 나온 모든 원아의 알림장이 생성된 뒤 삭제된다. 얼굴 임베딩과 텍스트 결과물은 자동 삭제 대상이 아니며, 원아 프로필을 지우거나 탈퇴하면 삭제된다. 얼굴 데이터는 제3자에게 제공하지 않는다. AI 생성 시에는 Anthropic(미국)에 위탁하며, 학습에 쓰이지 않고 최대 30일 후 삭제된다고 고지한다. Play 데이터 보안 항목은 '제3자 공유 없음, 전송 중 암호화, 삭제 요청 가능'이다. App Store에는 연결된 데이터로 사진·이메일·이름·사용자 ID·민감정보 등이 신고돼 있다. 추적에 대한 언급은 없다. 학부모 동의 확보 책임은 교사(회원)에게 있다. _(자사 정책 문서 기준. 스토어 설명에는 아직 '7일 후 자동 삭제'라는 옛 문구가 남아 있어 정책 문서(24시간)와 다르다.)_ [1](https://kidslog-web.vercel.app/privacy) [2](https://kidslog-web.vercel.app/terms) [3](https://play.google.com/store/apps/details?id=com.hunjun.kidslog&hl=ko&gl=KR) [4](https://apps.apple.com/kr/app/id6778382653)
- **주요 불만**: 미확인. App Store 리뷰 4개는 모두 5점 칭찬(사진 자동 분류·갤러리 폴더 저장 편리, 알림장 초안으로 시간 절약)이다. 리뷰가 출시 직후(6월 25~27일)에 몰려 있어 대표성이 낮다. 커뮤니티 불만은 검색되지 않았다. [1](https://apps.apple.com/kr/app/id6778382653)
- **기타**: 연간 포토북 관점에서는 유아반 교사용 B2B 앱이라 부모용 성장앨범과 사용 맥락이 다르다. 다만 '이름 한 번 등록 → 대량 업로드 → 인물별 자동 버킷(단체사진은 여러 아이에 중복 소속) → 잘못 묶이면 다른 아이로 옮겨 재학습' 흐름은 여러 아이(형제·쌍둥이) 가정의 인물별 사진 선택 단계 설계에 참고할 만하다. 서버에는 사진을 보관하지 않고(24시간 내 삭제) 결과를 기기 갤러리 폴더로 내보내는 '정리만 하고 저장은 로컬' 구조도 특징이다.

### Sponge - Gallery Cleaner

- **앱 정체** ✓: Sponge - Gallery Cleaner. 국문 Play 스토어에서도 영문 이름을 그대로 쓴다. Google Play: https://play.google.com/store/apps/details?id=com.prismtree.sponge , App Store: https://apps.apple.com/us/app/sponge-gallery-cleaner/id6738958624 . 패키지 ID, 개발자명 prismtree, 지원 이메일 support@prismtree.com이 Play와 App Store, 개발사 사이트에서 모두 같아 동일한 앱으로 판단했다. [1](https://play.google.com/store/apps/details?id=com.prismtree.sponge&hl=ko&gl=KR) [2](https://apps.apple.com/us/app/sponge-gallery-cleaner/id6738958624) [3](https://www.prismtree.com)
- **개발사·국가** ✓: PRISMTREE (prismtree). Play 개발자 정보의 주소는 인도 델리(53-H, DDA Flats, Mayur Vihar Phase 1, Delhi 110091)다. 자사 사이트는 스스로를 생산성·건강·일상 앱을 만드는 '인디 마이크로스타트업'으로 소개한다. 다른 앱으로 Aligned, Qik, Petals, Mizuki 등이 있다. _(개발사 성격 설명은 자사 출처)_ [1](https://play.google.com/store/apps/details?id=com.prismtree.sponge&hl=en&gl=US) [2](https://www.prismtree.com)
- **플랫폼**: Android(Google Play, 휴대폰·태블릿)와 iOS/iPadOS(17.6 이상) 모두 지원한다. App Store 기준으로 M1 이상 Mac에서도 실행된다. 웹 버전은 없다. [1](https://play.google.com/store/apps/details?id=com.prismtree.sponge&hl=ko&gl=KR) [2](https://apps.apple.com/us/app/sponge-gallery-cleaner/id6738958624)
- **핵심 기능**: 1) 스와이프 정리: 왼쪽은 삭제, 오른쪽은 유지. 2) 월별·앨범별·미디어 유형별(사진/동영상/스크린샷 등) 정리 모드와 할 일 목록식 진행 체크. 3) 중단한 지점부터 이어서 하기. 4) 무작위 정리 모드(한 번에 볼 장수 설정, 30/50/100장). 5) 스와이프하면서 원하는 폴더로 이동하거나 바로 공유하기. 6) 정리한 용량 등을 보여주는 통계 대시보드. [1](https://play.google.com/store/apps/details?id=com.prismtree.sponge&hl=ko&gl=KR) [2](https://apps.apple.com/us/app/sponge-gallery-cleaner/id6738958624)
- **관점 관련 기능** ✓: 자동 분류·인물 인식·유사/중복 묶기·베스트컷 추천은 없다. 사진 하나하나를 사람이 직접 판단하는 수동 선별 도구다. 흐름: (1) 정리 모드를 고른다(월별 / 앨범별 / 미디어 유형별 / 무작위). (2) 목록에서 월이나 앨범을 고른다. 이름·날짜·장수·크기로 정렬하거나 검색할 수 있고, 끝낸 항목은 숨길 수 있다. 각 항목에 진행 상태가 체크리스트처럼 표시된다. (3) 카드형 화면에서 한 장씩 왼쪽(삭제)이나 오른쪽(유지)으로 넘긴다. 버튼(✔️/❌)으로도 처리할 수 있고, 넘기면서 다른 폴더로 옮기거나 공유할 수 있다. (4) 진행 위치가 저장되어 나중에 이어서 할 수 있다. 무작위 모드는 30/50/100장 단위로 끊어서 보여줘 부담을 줄인다. yearbook 기획에 참고할 점: '월 단위 분할 + 이진(유지/제외) 스와이프 + 진행률 체크' 패턴은 1년치 사진에서 책에 넣을 사진을 고르는 흐름에 그대로 옮길 수 있다. 다만 결과는 삭제나 폴더 이동으로 남고, '선택 목록'이나 즐겨찾기로 남지는 않는다. _(중복·유사·흐린 사진 탐지가 없다는 점은 Play 사용자 리뷰에서 기능 요청으로 확인했다.)_ [1](https://apps.apple.com/us/app/sponge-gallery-cleaner/id6738958624) [2](https://play.google.com/store/apps/details?id=com.prismtree.sponge&hl=en&gl=US) [3](https://play.google.com/store/apps/details?id=com.prismtree.sponge&hl=ko&gl=KR)
- **AI 사용·처리 방식**: 스토어 설명에 AI나 이미지 인식 기능 언급이 없다. 정렬 기준은 메타데이터(날짜·크기·이름·앨범·미디어 유형)뿐이고, 처리는 모두 기기 안에서 한다고 밝힌다(업로드 없음). [1](https://apps.apple.com/us/app/sponge-gallery-cleaner/id6738958624) [2](https://play.google.com/store/apps/details?id=com.prismtree.sponge&hl=ko&gl=KR)
- **가격 모델** ✓: 부분 유료 모델(무료 + 인앱 결제)이다. 무료 플랜: 월별 정리, 사진 스와이프 무제한, 진행 저장. Premium 플랜: 동영상 정리, 앨범별·미디어 유형별 정리, 무작위 모드. iOS(US) 가격: 분기 $3.99, 연간 $9.99, 평생 $14.99, 가족용은 분기 $6.99·연간 $19.99·평생 $29.99이며 무료 체험이 있다. Android는 2026년 11월 Play 리뷰에 '구독 없이 평생 $3.50'이라는 언급이 있고, Play 페이지 데이터에서 $3.49 항목을 확인했다. _(Android 가격은 리뷰와 페이지 원시 데이터로만 확인했다. 한국 가격은 미확인.)_ [1](https://apps.apple.com/us/app/sponge-gallery-cleaner/id6738958624) [2](https://play.google.com/store/apps/details?id=com.prismtree.sponge&hl=en&gl=US)
- **평점·규모** ✓: Google Play: 평점 4.7, 리뷰 약 6,250개, 다운로드 50만 회 이상(카테고리 '도구'). App Store(US): 평점 4.8, 평가 32개. 개발사 설명에는 '전 플랫폼 90만 명 이상 사용'이라고 되어 있다. 순위 정보는 미확인. _(90만+ 사용자 수치는 자사 출처(스토어 설명))_ [1](https://play.google.com/store/apps/details?id=com.prismtree.sponge&hl=ko&gl=KR) [2](https://apps.apple.com/us/app/sponge-gallery-cleaner/id6738958624)
- **개인정보 처리**: 앱 설명상 사진은 기기에만 남고 업로드하지 않는다. Play 데이터 보안 항목: 제3자 공유 없음, 수집 가능 항목은 개인 정보·앱 활동·앱 정보 및 성능, 전송 중 암호화, 삭제 요청 가능. iOS 개인정보 라벨: 사용자와 연결되지 않는 사용 데이터·진단 데이터만 수집하고 추적 항목은 없다. 개발사 통합 개인정보처리방침(2026-10-15 갱신)은 여러 앱에 공통으로 적용되며, 이메일 등 개인정보와 사용 데이터를 수집할 수 있다고 적혀 있다. [1](https://play.google.com/store/apps/details?id=com.prismtree.sponge&hl=ko&gl=KR) [2](https://apps.apple.com/us/app/sponge-gallery-cleaner/id6738958624) [3](https://prismtree.com/privacy-policy)
- **주요 불만**: 읽은 리뷰는 대부분 긍정적이고 반복되는 강한 불만은 확인하지 못했다. 기능 요청이 주를 이룬다: 중복·유사·흐린 사진을 자동으로 찾아 한 번에 지우는 기능, 모든 폴더를 한 번에 제외하는 옵션, 스와이프 애니메이션 속도 조절, 용량 큰 순 정렬(iOS). _(스토어에 노출된 상위 리뷰만 확인했다. 부정 리뷰는 따로 수집하지 못했다.)_ [1](https://play.google.com/store/apps/details?id=com.prismtree.sponge&hl=en&gl=US) [2](https://play.google.com/store/apps/details?id=com.prismtree.sponge&hl=ko&gl=KR) [3](https://apps.apple.com/us/app/sponge-gallery-cleaner/id6738958624)
- **기타**: Sponge는 AI 없이 '월 단위 분할, 한 장씩 이진 판단, 진행률 체크리스트'만으로 Play 평점 4.7과 다운로드 50만 회 이상을 얻었다. 많은 사진을 작은 묶음(월별, 30/50/100장 단위)으로 나눠 부담을 줄이는 UX가 이 앱의 핵심 가치다. 1년치 사진에서 책에 넣을 사진을 고르는 yearbook 선택 단계에 참고할 만한 패턴이다. 반대로 사용자들이 중복·유사 묶기를 계속 요청하고 있어, 수동 스와이프만으로는 한계가 있다는 점도 드러난다.

### Favvy: Clean your photos

- **앱 정체** ✓: Favvy: Clean your photos (예전 이름 OnlyFavs). 한국어 스토어 페이지에도 영문 이름 그대로 나오며, 설명은 한국어로 번역되어 있다. Google Play: https://play.google.com/store/apps/details?id=com.kaikulabs.onlyfavs / iOS: https://apps.apple.com/us/app/id6743979781 (같은 법인). 스토어 카테고리는 도구(Tools), iOS는 Utilities. 공식 사이트는 favvyapp.com이다. [1](https://play.google.com/store/apps/details?id=com.kaikulabs.onlyfavs&hl=en&gl=US) [2](https://play.google.com/store/apps/details?id=com.kaikulabs.onlyfavs&hl=ko&gl=KR) [3](https://apps.apple.com/us/app/id6743979781)
- **개발사·국가** ✓: 브랜드는 Kaiku Labs이고, 법인은 THE SOFTWARE COMPANY OF BARCELONA S.L.(스페인 바르셀로나 Calle Bruc 149, NIF B26814830)이다. 이 법인은 iOS에서 Reemi, Mochi, Talkr 같은 다른 앱도 낸다. _(NIF는 자사 개인정보처리방침에서 가져왔다(자사 출처))_ [1](https://play.google.com/store/apps/details?id=com.kaikulabs.onlyfavs&hl=en&gl=US) [2](https://www.favvyapp.com/en/privacy) [3](https://apps.apple.com/us/app/id6743979781)
- **플랫폼**: Android(Google Play)와 iOS/iPadOS(iOS 16.4 이상, M1 이상 Mac과 visionOS에서도 실행 가능)를 지원한다. 웹 앱은 없고 웹사이트는 소개용이다. iOS는 한국어를 포함해 19개 언어를 지원한다. [1](https://apps.apple.com/us/app/id6743979781) [2](https://www.favvyapp.com)
- **핵심 기능**: 1) 스와이프 선별: 오른쪽으로 밀면 남기고 왼쪽으로 밀면 삭제 후보가 된다. 2) 모드별 정리: Random, 월별, Videos, Screenshots, Recents, Favorites, On This Day, 용량 큰 순(Heaviest), 앨범(폴더)별. 3) 중복·유사 사진 묶음(Duplicates 모드). 4) 세션 끝에 삭제 대상을 한 번에 검토한 뒤 확정하고, 진행 중 Undo가 된다. 5) 진행 상황과 확보한 용량 표시, 이어하기(이미 본 사진은 다시 보지 않음). 6) 연속 사용 보상(스트릭)과 추천인 보상. [1](https://play.google.com/store/apps/details?id=com.kaikulabs.onlyfavs&hl=en&gl=US) [2](https://apps.apple.com/us/app/id6743979781) [3](https://www.favvyapp.com)
- **관점 관련 기능** ✓: 흐름: 모드 선택(Random, 특정 월, 카테고리, 앨범, On This Day, Heaviest, Duplicates) → 사진을 한 장씩 카드로 띄워 좌우로 스와이프 → 세션이 끝나면 '삭제할 사진' 더미를 검토하고 확정 → Android는 시스템 삭제 흐름(Google Photos 휴지통, 삼성 갤러리 휴지통)을 거친다. 판단은 거의 전부 사용자가 한다. 앱이 자동으로 해 주는 부분은 기간·종류별 필터, 중복·유사 묶음(v3.3.1, 2026년 6월 추가. v3.6.4에서 '관련 없는 사진까지 묶던 문제'를 수정), 흐린 사진·어두운 사진·저화질 사진 정리(Play 설명에만 있고, 실제로 자동 감지하는지는 확인 못 함), 용량 큰 순 정렬 정도다. 인물이나 아이를 인식하는 기능, 베스트컷 추천, 점수 매기기는 없다. 웹사이트 후기에도 'would love a way to sort by people'이라는 요청이 실려 있다. 월별 모드와 '이어하기(이미 본 사진은 제외)'는 1년치 사진을 월 단위로 나눠 고르는 데 참고할 만하다. 다만 결과물이 '남길 사진 모음'이 아니라 '삭제'라는 점이 포토북용 선별과 다르다. 오른쪽 스와이프를 해도 별도 앨범이나 선택 목록에 담기지 않고 그냥 남겨질 뿐인지는 확인하지 못했다. _(모드 설명과 FAQ는 자사 웹사이트에서 가져왔다(자사 출처))_ [1](https://www.favvyapp.com) [2](https://apps.apple.com/us/app/id6743979781) [3](https://play.google.com/store/apps/details?id=com.kaikulabs.onlyfavs&hl=en&gl=US)
- **AI 사용·처리 방식**: AI나 머신러닝을 쓴다는 명시적인 설명은 없다. 중복·유사 묶음과 흐린 사진 정리를 어떤 방식으로 하는지도 공개되어 있지 않다. 사진 처리는 모두 기기 안에서 하고 오프라인으로 동작한다고 밝힌다(업로드 없음, 계정 없음, 서버 없음). _(온디바이스라는 주장은 자사 출처)_ [1](https://www.favvyapp.com) [2](https://www.favvyapp.com/en/privacy)
- **가격 모델** ✓: 무료로 쓸 수 있고 구독(PRO)이 있다. 무료판은 하루에 할 수 있는 스와이프 수가 제한되고, 스트릭과 추천인 보상으로 더 늘릴 수 있다. PRO는 스와이프 무제한, 고급 정렬 모드, 스트릭 보상을 준다. iOS(미국) 인앱 가격은 Weekly $4.99~5.99, Monthly $9.99, Yearly $14.99/$29.99/$34.99, Lifetime $49.99다. 다만 개발사는 2026년 2월 리뷰 답변에서 '일회성 구매는 제공하지 않는다'고 했다. Android의 원화 가격은 확인하지 못했다. _(무료 제한 방식은 개발사의 리뷰 답변과 자사 FAQ를 근거로 했다)_ [1](https://apps.apple.com/us/app/id6743979781) [2](https://www.favvyapp.com) [3](https://play.google.com/store/apps/details?id=com.kaikulabs.onlyfavs&hl=en&gl=US)
- **평점·규모** ✓: Google Play: 평점 3.6, 리뷰 816개, 다운로드 5만+(2026-11-25 조회). AppGoblin 추정치: 설치 약 8.6만, 월간 활성 사용자 약 6.1천 명, 월 매출 1만 달러 미만, 설치 증가 추세는 둔화(2025-07-27 출시). iOS(미국): 평점 4.7, 평가 95개. 자사 사이트는 '100K+ downloads'라고 주장한다. _(AppGoblin 수치는 추정치다. 100K+는 자사 출처)_ [1](https://play.google.com/store/apps/details?id=com.kaikulabs.onlyfavs&hl=en&gl=US) [2](https://appgoblin.info/apps/com.kaikulabs.onlyfavs) [3](https://apps.apple.com/us/app/id6743979781) [4](https://www.favvyapp.com)
- **개인정보 처리**: 사진은 기기 밖으로 나가지 않으며 업로드하거나 접근하지 않는다고 밝힌다(자사 정책). Play 데이터 보안 항목에는 '수집 데이터 없음'이라고 되어 있지만, 대략적 위치와 기기 ID를 광고·마케팅 목적으로 제3자와 공유할 수 있다고 함께 신고되어 있다. iOS 개인정보 라벨에는 위치와 사용 데이터를 추적에 쓸 수 있다고 나온다. AppGoblin이 찾아낸 SDK는 Countly, Firebase, RevenueCat, AppsFlyer, Facebook이다. [1](https://play.google.com/store/apps/datasafety?id=com.kaikulabs.onlyfavs&hl=en) [2](https://apps.apple.com/us/app/id6743979781) [3](https://www.favvyapp.com/en/privacy) [4](https://appgoblin.info/apps/com.kaikulabs.onlyfavs)
- **주요 불만**: Play 리뷰에서 반복되는 불만: 기능 대부분이 PRO 구독 뒤에 잠겨 있다, 삭제하려 할 때마다 결제 화면이 뜬다(30초마다 PRO 팝업이 뜬다는 표현도 있음), 무료판 제한이 심하다, 앱이 버벅인다, 구독 버튼을 찾기 어렵다. iOS에서는 일회성 구매가 없다는 점, 사진이 실제로 삭제되지 않는다는 점, 예전 버전의 크래시가 지적되었다. 업데이트 기록에도 삭제 오류와 메모리 문제를 고쳤다는 내용이 여러 번 나온다. _(스토어에 노출된 일부 리뷰만 봤다)_ [1](https://play.google.com/store/apps/details?id=com.kaikulabs.onlyfavs&hl=en&gl=US) [2](https://apps.apple.com/us/app/id6743979781)
- **기타**: 포토북 사진 선택 화면 기획에 참고할 점: Favvy는 '1장씩 좌우로 스와이프 → 세션 끝에 일괄 검토 → 확정'이라는 흐름과, 월별 모드와 '이어하기(이미 본 사진 제외)' 기능, 진행률과 스트릭을 묶어 많은 양을 지루하지 않게 고르게 만든다. 이 흐름은 '1년치 사진을 월별로 넘기며 넣을 사진을 고르는' 화면에 그대로 옮겨 쓸 만하다. 다만 인물·아이 인식이나 베스트컷 추천 같은 지능형 선별은 전혀 없고, 사용자도 인물별 정렬을 요청하고 있다. 또한 사이트와 FAQ는 'No ads, ever'라고 하는데, iOS 스토어 페이지에는 'Contains Advertising' 표시가 있고, 스토어에는 광고 목적의 데이터 공유와 추적이 신고되어 있다. 자사 주장과 스토어 신고 내용이 서로 맞지 않는다.
