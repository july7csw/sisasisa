from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .models import Words
from .models import Amounted_mentions
from .models import User_scrap
import pandas as pd
from django.contrib.auth import(authenticate, login as django_login, logout as django_logout)
import insertDB.rank10 as rank

# Create your views here.

def index(request):
    return render(request, 'news_infos/index.html')

def steady(request):
    # hits = Amounted_mentions.objects.filter(label='202008').order_by('-hits')[:10]
    # wordIdList = [w.wordId for w in hits]
    # words = []
    # for i in wordIdList:
    #     word = Words.objects.get(id=i)
    #     words.append(word.word)
    return render(request, 'news_infos/search.html')

def hot(request):
    words = rank.returnWord()
    return render(request, 'news_infos/hot.html', {'list': words})

def check_login(request):
    now_user = request.user
    if now_user.is_authenticated:
        logincheck = True
    else:
        logincheck = False
    return logincheck

def news_infos(request):
    return render(request, 'news_infos/index.html')


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
    # return render(request, 'words/hot_word.html', {'list': words})
    return render(request, 'news_infos/index.html', {'list': words})


def detail_word(request):
    word = Words.objects.get(word=request.__getattribute__('word'))
    meaning = word.__getattribute__('meaning')
    return render(request, 'words/detail_word.html', {'word': word, 'meaning': meaning})


def scrap(request):
    logincheck = check_login(request)
    if logincheck is True:
        list = User_scrap.objects.filter(user_Identifier=request.user)
        wordIdList = [w.wordId for w in list]
        words = []
        for i in wordIdList:
            word = Words.objects.get(id=i)
            words.append(word.word)
        return render(request, 'words/scrap.html', {'scrapList': words})
    else:
        return render(request, 'member/login.html')

def login(request):
    return render(request, 'member/login.html', {})

def logout(request):
    django_logout(request)
    return redirect('index')

def mypage(request):
    this_user =request.user
    message = "로그인이 필요한 페이지입니다."
    if this_user.is_authenticated:
        # user = User.objects.get(user=this_user)
        # print(user)
        user = "user 데이터를 가져온 뒤 처리"
        return render(request, 'member/mypage.html', {'user': user})
    else:
        return render(request, 'member/login.html', {'msg': message})