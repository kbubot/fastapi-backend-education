# Task8

- 주제: FastAPI 서버 맛보기

## 배우는 내용

- FastAPI first step
- Query Parameters

## 사전 요구사항

- `FastAPI`

## 태스크

> **참고** https://fastapi.tiangolo.com/tutorial/first-steps/

> **참고** https://fastapi.tiangolo.com/tutorial/query-params/

위 문서를 읽고, 쭉 따라해보세요.

그 이후에 다음 태스크를 수행하세요.

덧셈을 수행하는 API 를 생성합니다.
경로는 `sum` 이고, 입력은 쿼리스트링으로 받습니다.

- `/sum?a=1&b=2` : 3 이라는 적힌 문서를 반환
- `/sum?a=1&b=2&c=3` : 6 이라는 적힌 문서를 반환
- `/sum` : 입력이 필요하다는 텍스트 반환

로컬호스트에서 동작시키면 됩니다.
