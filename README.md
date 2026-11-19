# incident-agent

에러 로그나 장애 증상을 입력하면, AI 에이전트가 로그 검색·코드 조회·메트릭 확인을 단계별로 수행해
원인 추정과 조치안을 정리해 주는 서비스입니다.

## 스택

- Frontend: Next.js (반응형 웹, 추후 추가)
- Backend: Python, FastAPI
- DB: PostgreSQL (+ pgvector)
- Model: Claude API
- Infra: Docker Compose, AWS, GitHub Actions (추후 추가)

## 로드맵

1. FastAPI + PostgreSQL 기본 구조, 모델 호출 + 도구 1개(`search_logs`)로 에이전트 반복 구조 구현
2. 도구 확장(`read_code`, `get_metrics`, `find_similar_incident`), 비용·단계 수 제한, 재시도
3. Next.js 화면, 분석 과정 실시간 표시
4. 정답이 있는 장애 시나리오로 평가 세트 구성, 정확도 측정
5. 배포(AWS), CI/CD, 아키텍처 문서 정리

## 로컬 실행

```bash
cp .env.example .env        # 필요한 값 채우기 (API 키는 모델 호출 단계에서 필요)
docker compose up --build
curl http://localhost:8000/health
```

`{"status":"ok","env":"local","db":"up"}` 이 나오면 정상입니다.

## 주의

- 실제 회사 로그·코드·고객 데이터는 사용하지 않습니다. 공개 데이터셋이나 직접 만든 데모 앱의 로그만 사용합니다.
- API 키는 `.env`로만 관리하며 저장소에 커밋하지 않습니다.
