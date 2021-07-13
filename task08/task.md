#Task8
-주제: FastAPI 작업 환경 준비 및 사용해보기

##배우는 내용
1. FastAPI가 무엇인지 배운다.
2. FastAPI docs를 사용해본다.

##사전 요구사항
- 'fastAPI'
- 'uvicorn'

참고) https://soyoung-new-challenge.tistory.com/81

##테스크
- 'https://fastapi.tiangolo.com/ko/'
- 'https://soyoung-new-challenge.tistory.com/81'
위 문서를 참조하여, fastAPI를 익히고

task07에서 만든 API를 이용하여, fastAPI에서 구동되도록 만드세요. 

```python
...
from fastapi import FastAPI

app = fastAPI()

@app.get("/courses/{semester}")
async def get_courses(semester: int):
    ...
    #return response
```

