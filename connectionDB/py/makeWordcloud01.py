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
        print("워드클라우드를 만들 수 없는 단어:", word)

fileList = os.listdir(r"C:\Users\SW\sisasisa\sisasisa\static\wordCloud")

wordList = list(Words.objects.all().values())
print(fileList)

# for i in range(1, len(wordList)):
#     fileName = "wordCloud_"
#     word = wordList[i]['word']
#     fileName = fileName + word + ".png"

    # if fileName in fileList:
    #     print("리스트에 있음: ", word)
    #     continue
    # else:
    #     try:
    #         makeWordcloud(findWordId(word))
    #         print(i, "/", len(wordList), ":", word)
    #     except:
    #         print("오류남:", word)
    #         continue

# errorWord = ["손익분기점", "국제노동기구", "MRO", "ROE", "내부수익률", "듀레이션", "부채출자전환", "신용경색",
#              "합자회사", "자산부채이전", "CDO", "GSP", "공적부조", "PPP", "국제결제은행", "지방채", "MVNO",
#              "GPS", "ABCP", "COFIX", "파생결합증권", "ELF", "ETF", "상장지수펀드", "IRA", "LP", "역외선물환",
#              "장외시장", "리츠", "서킷브레이커", "스트레스 테스트", "신용평가", "팬더본드", "워런트"]
#
# for ew in errorWord:
#     makeWordcloud(findWordId(ew))