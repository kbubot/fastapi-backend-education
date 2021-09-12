# Task9

- 주제: FastAPI 서버에 스크래퍼 API 접목

## 배우는 내용

- Path Parameters
- Form Data
- 세션쿠키 처리

## 사전 요구사항

- `FastAPI`

## 테스크

> **참고** https://fastapi.tiangolo.com/tutorial/path-params/

> **참고** https://fastapi.tiangolo.com/tutorial/request-forms/

- task07에서 만든 API를 이용하여, 서버에서 사용하는 API처럼 구동되도록 만드세요.

```python
from fastapi import FastAPI, Form

app = fastAPI()

@app.post("/login/")
async def login(username: str = Form(...), password: str = Form(...)):
    ...
    #return response
    
@app.get("/courses/{semester}")
async def get_courses(semester: int):
    ...
    #return response
```
