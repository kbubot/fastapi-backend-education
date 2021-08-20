# async.py
import time
import requests
import unicodedata
from bs4 import BeautifulSoup
from typing import List
import aiohttp
import asyncio


# asynchronous
async def get_info(url):
    async with aiohttp.ClientSession() as session:  # 실제 요청을 비동기로
        async with session.get(url) as resp:
            html = await resp.text()
    soup = BeautifulSoup(html, 'html.parser')
    title = soup.select_one('div.header > h5').text
    content = soup.select_one('.content').text
    name = soup.select_one('li.name > span > span').text
    date = soup.select_one('li.date > time').text

    title = title.replace('\n', "")
    content = content.replace('\n', "")
    title = unicodedata.normalize("NFKD", title)
    content = unicodedata.normalize("NFKD", content)

    return [url, title, name, date, content]


async def get_notice_articles_async(page_num: int = 1) -> List[List[str]]:
    information = []
    req = requests.get('https://www.bible.ac.kr/ko/life/notice/list/' + str(page_num))
    html = req.content
    soup = BeautifulSoup(html, 'html.parser')
    urls = soup.select('.tbody')
    basic_url = "https://www.bible.ac.kr"
    for url in urls:
        combine = basic_url + url.select_one('.title > a')['href']
        information.append(get_info(combine))

    return await asyncio.gather(*information)


if __name__ == "__main__":
    start = time.time()
    data = asyncio.run(get_notice_articles_async(1))
    for i in data:
        print(i)
    print("실행 시간 :", time.time() - start)
