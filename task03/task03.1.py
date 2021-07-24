import requests
from bs4 import BeautifulSoup
from typing import List


def get_notice() -> List[List[str]]:
    req = requests.get('https://www.bible.ac.kr/ko/life/notice')
    information = []
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')
    first = soup.select('ul > li > span.loopnum')
    second = soup.select('ul > li > span.title')
    third = soup.select('ul > li > span.name')
    four = soup.select('ul > li > span.reg_date')
    num = 1
    while num < 21:
        information.append([first[num].text, second[num].text, third[num].text, four[num].text])
        num += 1
    return information


if __name__ == "__main__":
    informatiom = get_notice()
    for elements in informatiom:
        print(elements)
