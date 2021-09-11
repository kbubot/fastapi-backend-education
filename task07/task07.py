from typing import Dict, List, Optional
from dataclasses import dataclass
from bs4 import BeautifulSoup
import aiohttp
import asyncio


@dataclass
class SemesterData:
    year: int
    semester: int


FORM_DATA = {
    'username': "",
    'password': ""
}


async def get_courses(semester: Optional[SemesterData] = None) -> Dict[str, List[str]]:
    try:
        login_url = 'https://lms.bible.ac.kr/login/index.php' #로그인 하기 위한 url

        async with aiohttp.ClientSession() as session:
            await session.post(login_url, data=FORM_DATA) #f12-> Networt -> login_url -> Form Data에서 찾을 대로 로그인 양식 보내기

            if semester is None:
                choice_url = f"https://lms.bible.ac.kr/local/ubion/user/"  #로그인 후 semester에 맞는 대로 url이동
            else:
                choice_url = f"https://lms.bible.ac.kr/local/ubion/user/?year={semester.year}&semester={semester.semester}"

            req = await session.get(choice_url)  #url에서 정보 얻기
            html = await req.text
        soup = BeautifulSoup(html, 'html.parser')
        lists = soup.select('tbody.my-course-lists > tr')

        information = {}
        for list in lists:
            title = list.select_one('.coursefullname').text
            tutor = list.select_one('td')[2].text
            number = list.select('td')[3].text
            information[title] = [tutor, number]
        return information #정보 리턴
    except ValueError:
        print("로그인에 실패")


async def main():
    print("default")
    print(await get_courses())
    print("-" * 30)
    print(await get_courses(SemesterData(2021, 10)))  # 2020학년도 1학기 데이터 조회
asyncio.run(main())