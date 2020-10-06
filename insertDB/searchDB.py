import os
import django
import pandas as pd

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "djangoProject.settings")
django.setup()

from sisasisa.models import Words
from sisasisa.models import News_infos
from sisasisa.models import Amounted_mentions
from sisasisa.models import Assoicated_words
from sisasisa.models import User_scrap


def findWordName(wordID):
    word = Words.objects.get(id=wordID).word
    return word


def findWordId(word):
    wordId = Words.objects.get(word=word).id
    return wordId


def insertScrap(word, user_Identifier):
    wordId = findWordId(word)
    User_scrap.objects.create(
        wordId = wordId,
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


amounted_mention()