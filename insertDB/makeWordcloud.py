import matplotlib.pyplot as plt
import sys
from wordcloud import WordCloud
import pandas as pd
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "djangoProject.settings")
django.setup()

from sisasisa.models import Assoicated_words
from sisasisa.models import Words

word = "시사용어 받아오기"


def findWordId(keyword):
    wordId = Words.objects.get(word=keyword).id
    return wordId


assWordList, weightList = [], []


def findAssoAndWeight():
    data = list(Assoicated_words.objects.filter(wordId='804').values())
    for i in range(0, len(data)):
        weight = data[i]['weight']
        weight = float(weight)
        assWordList.append(data[i]['word'])
        weightList.append(weight)
    df = pd.DataFrame({'word': assWordList, 'weight': weightList})
    return df


# 연관어->데이터프레임
a = {}
wordId = findWordId(word)
data = findAssoAndWeight()
for k in range(0, len(data)):
    a.setdefault(data['word'][k], data['weight'][k])
print(a)

if sys.platform in ["win32", "win64"]:
    font_name = "malgun gothic"
    font_path = "c:/Windows/Fonts/malgun.ttf"
elif sys.platform == "darwin":
    font_name = "AppleGothic"
    font_path = "/Users/$USER/Library/Fonts/AppleGothic.ttf"
    WordCloud()

wordcloud = WordCloud(font_path='NotoSansKR-Bold.otf',
                      background_color="white",
                      max_words=100,
                      relative_scaling=0.3,
                      width=800,
                      height=400
                      ).generate_from_frequencies(a)
plt.figure(figsize=(15, 10))
plt.imshow(wordcloud)
plt.axis('off')
plt.savefig('wordcloud.png')
