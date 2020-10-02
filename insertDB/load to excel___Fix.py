import requests
import json
import pandas as pd
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "djangoProject.settings")
django.setup()

from sisasisa.models import News_infos
from sisasisa.models import Words

# 언급량 상위 단어만 뉴스 데이터 넣기
# xlsx2collect news data limit

filename = 'result_20190101_Amount_mention.xlsx'
data = pd.read_excel(filename)

wordIdList, cntList = data['wordId'], data['2019']

wordIdList2 = []

for i in range(0, len(wordIdList)):
    if data['2019'][i] >= 300:
        wordIdList2.append(data['wordId'][i])

print(len(wordIdList2))

monthList = []


def findWordName(wordId):
    word1 = Words.objects.get(id=wordId).word
    return word1


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


def findWord(wordId, startQuery, endQuery):
    data = {
        "access_key": "b4329809-2760-4e31-905f-bb2e59fdfd93",
        "argument": {
            "query": findWordName(wordId),
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
        saveNewsInfo(newsList, wordId)
    except:
        print(wordId, " : 오류")


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


for m in range(8, 9):
    month = findMonth(m)
    startDay = "01"
    endDay = findEndDay(m)
    startQuery = "2019-" + month + "-" + startDay
    endQuery = "2019-" + month + "-" + endDay
    for i in range(0, len(wordIdList2)):
        findWord(wordIdList2[i], startQuery, endQuery)
        print(i, "/", len(wordIdList2))
