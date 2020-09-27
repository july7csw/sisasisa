from django.shortcuts import render
from .models import Words
from .models import Amounted_mentions
import pandas as pd


# Create your views here.


def news_infos(request):
    return render(request, 'news_infos/index.html', {})


def word_list(request):
    words = Words.objects.all()
    return render(request, 'words/word_list.html', {'word_list': words})


def hot_word(request):

    words = Amounted_mentions.objects.filter(label='202008').order_by('-hits')[:9]
    return render(request, 'words/hot_word.html', {'hot_word': words})
