import pandas as pd
import os
import django
import math
from pandasql import *

from insertDB.searchDB import findWordName

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "djangoProject.settings")
django.setup()

# from sisasisa.models import Amounted_mentions
#
# amountList = list(Amounted_mentions.objects.all().values())
# df = pd.DataFrame(columns=['wordId', '2019'])
# wordList, labelList, hitList = [], [], []
# for i in range(0, len(amountList)):
#     wordId = amountList[i]['wordId']
#     word = findWordName(wordId)
#     label = amountList[i]['label']
#     hit = amountList[i]['hits']
#     wordList.append(word)
#     labelList.append(label)
#     hitList.append(hit)
#
# result = pd.DataFrame({'word': wordList, 'label': labelList, 'count': hitList})
# writer = pd.ExcelWriter('Amounted_mentions_df.xlsx', engine="openpyxl")
#
# result.to_excel(writer, sheet_name='Sheet1')
# writer.save()
# writer.close()


# nowYear = 2020
# nowMonth = 10
#
# def getStart(nowYear, nowMonth):
#     year = str(nowYear-1)
#     month = nowMonth
#     if month < 10:
#         month = "0" + str(month)
#     else:
#         month = str(month)
#     startDate = year + month
#     return startDate
#
# def getEnd(nowYear, noyMonth):
#     year = str(nowYear)
#     month = nowMonth-2
#     if month < 10:
#         month = "0" + str(month)
#     else:
#         month = str(month)
#     endDate = year + month
#     return endDate
#
#
# data = pd.read_excel('Amounted_mentions_df.xlsx')
# wordList = data['word']
# wordList = list(set(wordList))
#
# avgList = []
# startDate = getStart(nowYear, nowMonth)
# endDate = getEnd(nowYear, nowMonth)
#
# for s in range(0, len(wordList)):
#     sql1 = "select avg(count) as avg from data where word='" + wordList[s] + "' and label>='" + startDate +"' and label<='" + endDate +"'"
#     print(s, "/", len(wordList), ":", sql1)
#     try:
#         avg = sqldf(sql1, locals())['avg'][0]
#         avg = round(avg, 1)
#     except:
#         avg = 0
#     avgList.append(avg)
#
# result = pd.DataFrame({'word': wordList, 'avg': avgList})
# result.to_excel('Amounted_mentions_avg', sheet_name='Sheet1')

# data1 = pd.read_excel('Amounted_mentions_df.xlsx', sheet_name="Sheet1")
# data2 = pd.read_excel('Amounted_mentions_df.xlsx', sheet_name="avg")
# wordList = data2['word']
# count202009 = []
# for w in range(0, len(wordList)):
#     print(w, "/", len(wordList))
#     try:
#         sql = "select count from data1 where label=202009 and word='" + wordList[w] +"'"
#         cnt = sqldf(sql, locals())['count'][0]
#     except:
#         cnt = 0
#     count202009.append(cnt)
#
# result = pd.DataFrame({'word': wordList, 'cnt_202009': count202009})
# result.to_excel('Amounted_mentions_compare.xlsx', sheet_name='Sheet1')





