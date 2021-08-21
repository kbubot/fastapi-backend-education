# thread.py
import time
import requests
import unicodedata
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor
from typing import List


def get_plus_url(page_num) -> List[str]:
    data = []
    url = 'https://www.bible.ac.kr/ko/life/notice/list/' + str(page_num)
    req = requests.get(url)
    html = req.content
    soup = BeautifulSoup(html, 'html.parser')
    urls = soup.select('.tbody')

    for url in urls:
        data.append(url.select_one('.title > a')['href'])

    return data


def get_information(plus_link) -> List[List[str]]:
    link = "https://www.bible.ac.kr" + plus_link
    req = requests.get(link)
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')
    title = soup.select_one('div.header > h5').text
    content = soup.select_one('.content').text
    name = soup.select_one('li.name > span > span').text
    date = soup.select_one('li.date > time').text

    title = title.replace('\n', "")
    content = content.replace('\n', "")
    title = unicodedata.normalize("NFKD", title)
    content = unicodedata.normalize("NFKD", content)

    return [link, title, name, date, content]


def get_notice_articles_process(page_num: int = 1) -> List[List[str]]:
    information = []
    links = get_plus_url(page_num)
    with ThreadPoolExecutor() as executor:
        for link in links:
            information.append(executor.submit(get_information, link))

    return information


if __name__ == "__main__":
    start = time.time()
    data = get_notice_articles_process(1)
    for i in data:
        print(i.result())
    print("실행 시간(초) :", time.time() - start)
