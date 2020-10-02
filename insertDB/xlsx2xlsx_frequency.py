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


# 수정~~~~~~~~~

amountList = list(Amounted_mentions.objects.filter(label__startswith='2019').values())

df = pd.DataFrame(columns=['wordId', '2019'])

wordIdList, cntList, reWordIdList = [], [], []

for i in range(0, len(amountList)):
    wordIdList.append(amountList[i]['wordId'])
    cntList.append(amountList[i]['hits'])


def findWordMeaning(wordId):
    meaning = Words.objects.get(id=wordId).meaning
    return meaning


reWordIdList.append(wordIdList[0])
j = 0
cnt = 0

for i in range(0, len(wordIdList)):
    wordId = wordIdList[i]
    hits = cntList[i]
    cnt += hits
    meaning1 = findWordMeaning(wordIdList[i])
    if meaning1.__ne__(findWordMeaning(reWordIdList[j])):
        df.loc[j] = wordId, cnt
        reWordIdList.append(wordIdList[i])
        j += 1
        cnt = 0
    print(i, "/", len(wordIdList))

writer = pd.ExcelWriter('C:/Users/myth8/PycharmProjects/django_first/insertDB/test.xlsx',
                        engine="openpyxl")

df.to_excel(writer, sheet_name='sheet1')
writer.save()
writer.close()
