from typing import List, Dict
from collections import defaultdict
import json
import requests


def get_konkuk_movie_info(date: str) -> Dict[str, List[List[str]]]:
    information = defaultdict(list)
    url = "https://www.lottecinema.co.kr/LCWS/Ticketing/TicketingData.aspx"
    dic = {
        "MethodName": "GetPlaySequence",
        "channelType": "MA",
        "osType": "",
        "osVersion": "",
        "playDate": date,
        "cinemaID": "1|0001|1008",
        "representationMovieCode": ""}

    parameter = {"paramList": json.dumps(dic)}
    response = requests.post(url, data=parameter).json()
    datas = response['PlaySeqs']['Items']

    for data in datas:
        name = data["MovieNameKR"]
        start_time = data["StartTime"]
        end_time = data["EndTime"]
        information[name].append([start_time, end_time])
    return information


if __name__ == '__main__':
    get = get_konkuk_movie_info("2021-08-05")
    print(get)