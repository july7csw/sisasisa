import requests
import json
import re
import pandas as pd
import os
import django
from datetime import datetime

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "djangoProject.settings")
django.setup()

from sisasisa.models import Amounted_mentions
from sisasisa.models import Words

filename = 'sisa_term_20200924.xlsx'
data = pd.read_excel(filename, sheet_name='Sheet1')
wordList = data['word']
wordIdList, hitsList, errorList = [], [], []


# df = pd.DataFrame()

# writer = pd.ExcelWriter('C:/Users/myth8/PycharmProjects/django_first/insertDB/result_20190101_Amount_mention.xlsx',
#                         engine="openpyxl")


def findWordId(keyword):
    wordId = Words.objects.get(word=keyword).id
    return wordId


def findTimeLine(query, start, end, false=None):
    # temp_df = pd.DataFrame()

    data = {
        "access_key": "b4329809-2760-4e31-905f-bb2e59fdfd93",
        "argument": {
            "query": query,
            "published_at": {
                "from": start,
                "until": end
            },
            "provider": [
                "",
            ],
            "category": [
                "",
            ],
            "category_incident": [
                "",
            ],
            "byline": "",
            "interval": "month",
            "normalize": false
        }
    }
    try:
        url = "http://tools.kinds.or.kr:8888/time_line"
        res = requests.post(url, data=json.dumps(data))
        timeline = res.json()['return_object']['time_line']
        for i in range(0, len(timeline)):
            # hitsList = []
            label = timeline[i]['label']
            hits = timeline[i]['hits']
            wordId = findWordId(query)
            # hitsList.append(hits)
            Amounted_mentions.objects.create(
                wordId=wordId,
                label=label,
                hits=hits
            )
            # temp_df[label] = hitsList
        # return temp_df

    except:
        errorList.append(query)


for j in range(0, len(wordList)):
    # temp_df = findTimeLine(str(wordList[j]), "2019-01-01", "2019-12-31")
    findTimeLine(wordList[j], "2019-01-01", "2020-09-30")
    # df = df.append(temp_df)

print("end!")

#
# df.to_excel(writer, sheet_name='sheet1')
# writer.save()
# writer.close()
