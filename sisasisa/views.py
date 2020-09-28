from django.shortcuts import render
from .models import Words
from .models import Amounted_mentions
from .models import User_scrap
import pandas as pd


# Create your views here.


def news_infos(request):
    return render(request, 'news_infos/index.html', {})


def word_list(request):
    words = Words.objects.all()
    return render(request, 'words/word_list.html', {'word_list': words})


def hot_word(request):
    hits = Amounted_mentions.objects.filter(label='202008').order_by('-hits')[:10]
    wordIdList = [w.wordId for w in hits]
    words = []
    for i in wordIdList:
        word = Words.objects.get(id=i)
        words.append(word.word)
    return render(request, 'words/hot_word.html', {'list': words})


def scrap(request):
    list = User_scrap.objects.filter(user_Identifier=request.user)
    wordIdList = [w.wordId for w in list]
    words = []
    for i in wordIdList:
        word = Words.objects.get(id=i)
        words.append(word.word)
    return render(request, 'words/scrap.html', {'scrapList': words})
