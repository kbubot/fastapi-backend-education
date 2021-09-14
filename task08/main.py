from typing import Optional

from fastapi import FastAPI

app = FastAPI()


@app.get("/sum/")
async def read_sum(a: Optional[int] = None, b: Optional[int] = None, c: int = 0):
    if a is None:
        return "입력이 필요하다"
    if b is None:
        return "입력이 더 필요하다"
    sum_value = a + b + c
    return sum_value


