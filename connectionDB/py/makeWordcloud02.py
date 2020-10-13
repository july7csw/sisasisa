import os
import django
from pathlib import Path
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import font_manager

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "djangoProject.settings")
django.setup()

from sisasisa.models import Words
from sisasisa.models import Assoicated_words

font_fname = 'C:/Windows/Fonts/NanumGothic.ttf'
font_family = font_manager.FontProperties(fname=font_fname).get_name()
plt.rcParams["font.family"] = font_family

def findWordName(wordId):
    word = Words.objects.get(id=wordId).word
    return word

def findSynonym(wordId):
    synonymIdList = []
    meaning = list(Words.objects.filter(id=wordId).values('meaning'))
    meaning = meaning[0]['meaning']
    synonym = list(Words.objects.filter(meaning=meaning).values('id'))
    for sn in synonym:
        if sn == wordId:
            continue
        else:
            synonymIdList.append(sn)
    return synonymIdList

def findWordIdList(keyword):
    wordIdList = []
    wordId = list(Words.objects.filter(word=keyword).values('id'))
    for wi in wordId:
        wordIdList.append(wi['id'])
    return wordIdList

def findAssoAndWeight(wordId):
    assWordList, weightList = [], []
    data = list(Assoicated_words.objects.filter(wordId=wordId).values())
    for i in range(0, len(data)):
        weight = data[i]['weight']
        weight = float(weight)
        assWordList.append(data[i]['word'])
        weightList.append(weight)
    df = pd.DataFrame({'word': assWordList, 'weight': weightList})
    return df

def makeWordcloud1(wordId):
    data = findAssoAndWeight(wordId)
    word = findWordName(wordId)

    if len(data) > 0:
        makeWordcloud2(data, word)
    else:
        wordIdList = findSynonym(wordId)
        if len(wordIdList) == 1:
            pass
        else:
            for wl in wordIdList:
                print("단어: ", findWordName(wl['id']))
                data = findAssoAndWeight(wl['id'])
                if len(data) > 0:
                    makeWordcloud2(data, word)
                else:
                    print("연관어 없음")
                    continue

def makeWordcloud2(data, word):
    a = {}
    filePath = r"C:\Users\SW\sisasisa\sisasisa\static\wordCloud"
    print(filePath)
    for k in range(0, len(data)):
        a.setdefault(data['word'][k], data['weight'][k])

    fileName = filePath + 'wordCloud_' + str(word).strip() + '.png'

    font_path = r"C:\Users\SW\sisasisa\sisasisa\static\NotoSansKR-Bold.otf"

    WordCloud()
    wordcloud = WordCloud(font_path=font_path,
                          background_color="white",
                          max_words=100,
                          relative_scaling=0.3,
                          width=800,
                          height=400
                          ).generate_from_frequencies(a)
    plt.figure(figsize=(15, 10))
    plt.imshow(wordcloud)
    plt.axis('off')
    plt.savefig(fileName)
    plt.close()


fileList = os.listdir(r"C:\Users\SW\sisasisa\sisasisa\static\wordCloud")

wordList = list(Words.objects.all().values())

for i in range(1, len(wordList)):
    fileName = "wordCloud_"
    word = wordList[i]['word']
    fileName = fileName + word + ".png"

    if fileName in fileList:
        continue
    else:
        wordIdList = findWordIdList(word)
        for wil in wordIdList:
            makeWordcloud1(wil)
