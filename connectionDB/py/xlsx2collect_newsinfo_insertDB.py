import requests
import json
import re
import pandas as pd
import os
import django
from datetime import datetime

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "djangoProject.settings")
django.setup()

from sisasisa.models import News_infos
from sisasisa.models import Words

filename = '../xlsx/sisa_term_20200924.xlsx'
data = pd.read_excel(filename, sheet_name='Sheet1')
wordList = data['word']
meaningList = data['meaning']

monthList, countList = [], []


def findWordId(keyword):
    wordId = Words.objects.get(word=keyword).id
    return wordId


def saveNewsInfo(newsList, wordId):
    for j in range(0, len(newsList)):
        a = newsList[j]['news_id']
        b = newsList[j]['provider']
        c = newsList[j]['category']
        d = newsList[j]['provider_link_page']
        e = newsList[j]['published_at']
        News_infos.objects.create(
            wordId=wordId,
            news_id=a,
            provider=b,
            category=c,
            provider_link_page=d,
            published_at=e
        )


def findWord(keyword, startQuery, endQuery):
    data = {
        "access_key": "b4329809-2760-4e31-905f-bb2e59fdfd93",
        "argument": {
            "query": keyword,
            "published_at": {
                "from": startQuery,
                "until": endQuery
            },
            "provider": [
                "",
            ],
            "category": [
                ""
            ],
            "category_incident": [
                ""
            ],
            "byline": "",
            "provider_subject": [
                ""
            ],
            "subject_info": [
                ""
            ],
            "subject_info1": [
                ""
            ],
            "subject_info2": [
                ""
            ],
            "subject_info3": [
                ""
            ],
            "subject_info4": [
                ""
            ],
            "sort": {"date": "desc"},
            "hilight": 200,
            "return_from": 0,
            "return_size": 10000,
            "fields": [
                "byline",
                "category",
                "provider_link_page",
                "provider_news_id"
            ]
        }
    }
    try:
        url = "http://tools.kinds.or.kr:8888/search/news"
        res = requests.post(url, data=json.dumps(data))
        newsList = res.json()['return_object']['documents']
        keyword2 = str(keyword).split(" OR")[0]
        print(keyword2)
        wordId = findWordId(keyword2)
        saveNewsInfo(newsList, wordId)

    except:
        count = "오류남"


def findMonth(m):
    if m < 10:
        month = "0" + str(m)
    else:
        month = str(m)
    return month


def findEndDay(m):
    if m == 1 or m == 3 or m == 5 or m == 7 or m == 8 or m == 10 or m == 12:
        endDay = "31"
    elif m == 2:
        endDay = "28"
    else:
        endDay = "30"
    return endDay


for m in range(7, 8):
    month = findMonth(m)
    startDay = "01"
    endDay = findEndDay(m)
    startQuery = "2019-" + month + "-" + startDay
    endQuery = "2019-" + month + "-" + endDay
    for i in range(0, len(wordList)):
        keyword = wordList[i]
        if meaningList[i].__eq__(meaningList[i + 1]) and i < len(wordList):
            keyword = wordList[i] + " OR " + wordList[i + 1]
            findWord(keyword, startQuery, endQuery)
        elif i != 0 and meaningList[i].__eq__(meaningList[i - 1]):
            i = i + 1
        else:
            findWord(keyword, startQuery, endQuery)
        print(month, "월 : ", i, "/", len(wordList))