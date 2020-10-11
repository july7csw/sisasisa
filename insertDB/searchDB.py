import os
import django
import pandas as pd
from django.db.models import Count

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "djangoProject.settings")
django.setup()

from sisasisa.models import Words
from sisasisa.models import News_infos
from sisasisa.models import Amounted_mentions
from sisasisa.models import Assoicated_words
from sisasisa.models import User_scrap


def findScrapList(word, user_Identifier):
    print(word, "데이터 찾기 실행")
    wordId = findWordId(word)
    data = User_scrap.objects.filter(wordId=wordId, user_Identifier=user_Identifier).values()
    if data.exists():
        return True
    return False


def findMeaning(wordId):
    data = Words.objects.filter(id=wordId).values()
    meaning = (data[0]['meaning'])
    return meaning


def findWordName(wordID):
    word = Words.objects.get(id=wordID).word
    return word


def findWordId(word):
    wordId = Words.objects.get(word=word).id
    return wordId


def insertScrap(word, user_Identifier):
    print(word, "데이터 넣기 실행")
    wordId = findWordId(word)
    User_scrap.objects.create(
        wordId=wordId,
        user_Identifier=user_Identifier
    )


def amounted_mention():
    amountList = list(Amounted_mentions.objects.all().values())
    df = pd.DataFrame(columns=['wordId', 'Amount'])

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
            df.loc[j] = wordIdList[i - 1], cnt
            wordId = wordIdList[i]
            cnt = cntList[i]
            j += 1
    df.loc[j] = wordId, cnt

    df = df.sort_values(by="Amount", ascending=False).head(10)

    wordIdList2 = list(df['wordId'])
    wordAmtList = list(df['Amount'])
    wordNameList = []

    for i in range(0, len(wordIdList2)):
        wordNameList.append(findWordName(wordIdList2[i]))

    finDf = pd.DataFrame({'word': wordNameList, 'amt': wordAmtList})

    writer = pd.ExcelWriter('202009_steady10.xlsx', engine="openpyxl")

    finDf.to_excel(writer, sheet_name='123')
    writer.save()
    writer.close()


def deleteScrap(word, user_Identifier):
    wordId = findWordId(word)
    deleteWord = User_scrap.objects.get(wordId=wordId, user_Identifier=user_Identifier)
    deleteWord.delete()


# steady category
def findCategoryRank(category):
    if len(category) != 0:
        newsInfo = News_infos.objects.filter(category__icontains=category).values('wordId')
    else:
        newsInfo = News_infos.objects.all().values('wordId')
    return createCategoryDF(newsInfo)


def createCategoryDF(newsInfo):
    newsInfo = newsInfo.annotate(count=Count('wordId'))
    wordList, CntList = [], []
    for i in range(0, len(newsInfo)):
        wordList.append(findWordName(newsInfo[i]['wordId']))
        CntList.append(newsInfo[i]['count'])
    df = pd.DataFrame({'word': wordList, 'count': CntList})

    df = df.sort_values(by='count', ascending=False)
    finDf = df.head(10)
    print(finDf)


# findCategoryRank('사회')
# findCategoryRank2()

def findCategoryRank3():
    wordList = Words.objects.all().wordId
    categoryList = ['사회', '경제', '문화', 'IT']
    for i in range(0, len(categoryList)):
        newsInfo = News_infos.objects.filter(published_at__range=["2019-09-01", "2020-08-31"],
                                             category__icontains=categoryList[i]).values('wordId')
        createCategoryDF(newsInfo).to_excel('hotWordAvg.xlsx', sheet_name=categoryList[i])

def createCategoryDF(newsInfo):
    newsInfo = newsInfo.annotate(count=Count('wordId'))
    wordList, CntList = [], []
    for i in range(0, len(newsInfo)):
        wordList.append(findWordName(newsInfo[i]['wordId']))
        CntList.append(newsInfo[i]['count']/12)
    df = pd.DataFrame({'word': wordList, 'avg': CntList})

    df = df.sort_values(by='count', ascending=False)
    finDf = df.head(60)
    return finDf
