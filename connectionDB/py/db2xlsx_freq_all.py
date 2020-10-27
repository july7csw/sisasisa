import os
import django
from pandasql import *

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
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

# def getNewsInfo(start, end, category):
#     newsInfo = News_infos.objects.filter(published_at__range=[start, end], category__icontains=category).values('wordId')
#     return newsInfo
#
# def makeAvgDF(querySet):
#     wordList, cntList = [], []
#     for j in range(0, len(querySet)):
#         wordList.append(findWordName(querySet[j]['wordId']))
#         cntList.append(querySet[j]['count']/12)
#     df = pd.DataFrame({'word': wordList, 'avg': cntList})
#     return df
#
# def makeCntDF(querySet):
#     wordList, cntList = [], []
#     for j in range(0, len(querySet)):
#         wordList.append(findWordName(querySet[j]['wordId']))
#         cntList.append(querySet[j]['count'])
#     df = pd.DataFrame({'word': wordList, 'cnt': cntList})
#     return df
#
# def makeHotRank():
#     categoryList = ['사회', '경제', '문화', 'IT']
#     writer = pd.ExcelWriter('hotWordCompare.xlsx', engine='openpyxl')
#     for i in range(0, len(categoryList)):
#         avgInfo = getNewsInfo("2019-09-01", "2020-08-31", categoryList[i])
#         avgInfo = avgInfo.annotate(count=Count('wordId'))
#         cntInfo = getNewsInfo("2020-09-01", "2020-09-30", categoryList[i])
#         cntInfo = cntInfo.annotate(count=Count('wordId'))
#         avgDF = makeAvgDF(avgInfo)
#         cntDF = makeCntDF(cntInfo)
#         cntSheet = categoryList[i] + "cnt"
#         avgDF.to_excel(writer, sheet_name=categoryList[i])
#         cntDF.to_excel(writer, sheet_name=cntSheet)
#         writer.save()
#     writer.close()
#
# makeHotRank()


#data = pd.read_excel('hotWordCompare.xlsx', sheet_name="Sheet1")

# wordList = []
# words = Words.objects.all().values('word')
# for i in range(1, len(wordList)):
#     word = wordList[i]['word']
#     wordList.append(word)
#
# def makeCnt(df, value, word):
#     word1 = df['word']
#     cnt1 = df[value]
#     cntList_f = []
#     for j in range(0, len(word1)):
#         if word in word1[j]:
#             cntList_f.append(cnt1[j])
#         else:
#             cntList_f.append(0)
#     return cntList_f
#
# def findValue(word):
#     categoryList = ['사회', '경제', '문화', 'IT']
#     for cl in categoryList:
#         writer = pd.ExcelWriter('hotWordCompare_f.xlsx', engine='openpyxl')
#         data1 = pd.read_excel('hotWordCompare.xlsx', sheet_name=cl)
#         avgList = makeCnt(data1, 'avg', word)
#         sheetName = cl + "cnt"
#         data2 = pd.read_excel('hotWordCompare.xlsx', sheet_name=sheetName)
#         cntList = makeCnt(data2, 'cnt', word)
#         df = pd.DataFrame({'word': wordList, 'avg': avgList, 'cnt': cntList})
#         df.to_excel(writer, sheet_name=categoryList[i])
#         writer.save()
#     writer.close()
#     return None
#
# for k in range(1, len(wordList)):
#     findValue(wordList[k])
