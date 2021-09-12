import requests
from bs4 import BeautifulSoup
from typing import List
import unicodedata


def get_notice_articles(page_num: int) -> List[List[str]]:
    info: List[List[str]] = []
    req = requests.get('https://www.bible.ac.kr/ko/life/notice/list/' + str(page_num))
    html = req.content
    soup = BeautifulSoup(html, 'html.parser')
    links = soup.select('span.title > a[href]')
    titles = soup.select('li > span.title > a')
    names = soup.select('li > span.name')
    days = soup.select('li > span.reg_date')
    num = 0
    while num < 20:
        link = "https://www.bible.ac.kr/" + links[num]['href']
        title = titles[num].text
        name = names[num + 1].text
        day = days[num + 1].text
        info.append([link, title, name, day])
        contents = requests.get(info[num][0])
        copy = BeautifulSoup(contents.content, 'html.parser')
        main_text = copy.select_one('head > meta[name="description"]')['content']
        main_text = unicodedata.normalize("NFKD", main_text)
        info[num].append(main_text)
        num += 1
    return info


if __name__ == "__main__":
    info: List[List[str]] = get_notice_articles(4)
    for element in info:
        print(element)
