import pandas as pd
import os
import django
import math

from insertDB.searchDB import findWordName

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "djangoProject.settings")
django.setup()

from sisasisa.models import Amounted_mentions

amountList = list(Amounted_mentions.objects.filter(label__startswith='2019').values())

df = pd.DataFrame(columns=['wordId', '2019'])


wordIdList, cntList = [], []

for i in range(0, len(amountList)):
    wordIdList.append(amountList[i]['wordId'])
    cntList.append(amountList[i]['hits'])

cnt = cntList[0]
wordId = wordIdList[0]
j = 0

for i in range(1, len(wordIdList)):
    if wordId.__eq__(wordIdList[i]):
        cnt += cntList[i]
    elif wordId.__ne__(wordIdList[i]):
        df.loc[j] = wordIdList[i - 1], math.ceil(cnt / 12)
        wordId = wordIdList[i]
        cnt = cntList[i]
        j += 1
df.loc[j] = wordId, math.ceil(cnt / 12)

# 월별 데이터

labelList = ['202001', '202002', '202003', '202004', '202005', '202006', '202007', '202008', '202009']
df2 = pd.DataFrame(columns=['wordId'])


def monthly_data(label):
    amountList = list(Amounted_mentions.objects.filter(label=label).values())
    df = pd.DataFrame(columns=['wordId', label])
    wordIdList, cntList = [], []
    for i in range(0, len(amountList)):
        wordIdList.append(amountList[i]['wordId'])
        cntList.append(amountList[i]['hits'])
    cnt = cntList[0]
    wordId = wordIdList[0]
    j = 0
    for i in range(1, len(wordIdList)):
        if wordId.__eq__(wordIdList[i]):
            cnt += cntList[i]
        elif wordId.__ne__(wordIdList[i]):
            df.loc[j] = wordId, cnt
            wordId = wordIdList[i]
            cnt = cntList[i]
            j += 1
    cntList.append(cnt)
    df.loc[j] = wordId, cnt
    return df


for i in range(0, len(labelList)):
    df2 = pd.merge(df2, monthly_data(labelList[i]), how='outer', on='wordId')

df3 = pd.merge(df, df2, how='outer', on='wordId').fillna(0)

calcList = []
calcData = pd.DataFrame({'wordId': df3['wordId']})
orgData = df3['2019']

for i in range(0, len(labelList)):
    for j in range(0, len(df3)):
        result = df3[labelList[i]][j] - round(orgData[j] / (1 + i))
        orgData[j] += df3[labelList[i]][j]
        calcList.append(result)
    calcData[labelList[i]] = calcList
    calcList.clear()

rank10 = calcData.sort_values(by='202009', ascending=False)
rank10 = rank10.head(1000)

# print(rank10)

wordIdList2 = list(rank10['wordId'])
numList = list(rank10['202009'])

wordList = []

for i in range(0, len(wordIdList2)):
    word = findWordName(wordIdList2[i])
    wordList.append(word)

finDf = pd.DataFrame({'word': wordList, 'cnt': numList})

writer = pd.ExcelWriter('202009_rank10_f.xlsx', engine="openpyxl")

finDf.to_excel(writer, sheet_name='123')
writer.save()
writer.close()
