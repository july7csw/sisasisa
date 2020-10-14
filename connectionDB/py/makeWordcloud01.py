import os
import django
from pathlib import Path
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import pandas as pd

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "djangoProject.settings")
django.setup()

from sisasisa.models import Words
from sisasisa.models import Assoicated_words

def findWordName(wordId):
    word = Words.objects.get(id=wordId).word
    return word

def findWordId(keyword):
    wordId = list(Words.objects.filter(word=keyword).values('id'))
    wordId = wordId[0]['id']
    return wordId

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

def makeWordcloud(wordId):
    a = {}
    filePath = str(Path(__file__).parent.parent) + "\\sisasisa\\static\\wordCloud\\"
    word = findWordName(wordId)
    data = findAssoAndWeight(wordId)
    if len(data) > 0:
        for k in range(0, len(data)):
            a.setdefault(data['word'][k], data['weight'][k])

        fileName = filePath + 'wordCloud_' + str(word).strip() + '.png'

        font_path = str(Path(__file__).parent.parent) + "\\sisasisa\\static\\NotoSansKR-Bold.otf"

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
    else:
        ("워드클라우드를 만들 수 없는 단어:", word)

fileList = os.listdir(r"C:\Users\SW\sisasisa\sisasisa\static\wordCloud")

wordList = list(Words.objects.all().values())
(fileList)
