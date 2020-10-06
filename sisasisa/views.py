from django.contrib.auth import (logout as django_logout, get_user_model)
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.db.models import Q


import insertDB.rank10 as rank
from .models import User_scrap
from .models import Words
from user.models import User


# Create your views here.

def index(request):
    return render(request, 'news_infos/index.html')

def steady(request):
    words = rank.returnSteadyWord()
    return render(request, 'news_infos/steady.html', {'words': words})

def hot(request):
    words = rank.returnHotWord()
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
    hotWords = rank.returnHotWord()
    steadyWords = rank.returnSteadyWord()
    return render(request, 'news_infos/index.html', {'steadyWords': steadyWords, 'hotWords': hotWords})


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
        return render(request, 'member/../user/templates/user/login.html')


def login(request):
    return render(request, 'member/../user/templates/user/login.html', {})


# def logout(request):
#     return HttpResponseRedirect(request.POST['path'])
    # django_logout(request)
    # return redirect('index')


def mypage(request):
    this_user = request.user
    message = "로그인이 필요한 페이지입니다."
    if this_user.is_authenticated:
        print(request.user.email)
        user = "user 데이터를 가져온 뒤 처리"
        return render(request, 'member/mypage.html', {'user': user})
    else:
        return redirect('user/login')

        # return render(request, 'member/login.html', {'msg': message})

def search(request):
    keyword = request.GET.get('keyword', '')
    words = Words.objects.all()
    if not keyword:
        keyword = """' '"""
        return render(request, 'news_infos/search.html', {'notWord': keyword})
    else:
        inWord = words.filter(word__icontains=keyword)
        inMeaning = words.filter(
            Q(meaning__icontains=keyword) & ~Q(word__icontains=keyword)
        )
        if inWord.exists() is False and inMeaning.exists() is False:
            return render(request, 'news_infos/search.html', {'notWord': keyword})
        else:
            meaningList = [im.meaning for im in inMeaning]
            inMeaning_mean = []
            for ml in meaningList:
                keywordIndex = ml.find(keyword)
                startIndex = ml[:keywordIndex].rfind(".")
                previewText = ml[startIndex+2:]
                inMeaning_mean.append(previewText)
            inMeaning_word = [im.word for im in inMeaning]
            meaningResult = [ x for x in zip(inMeaning_word, inMeaning_mean)]
            return render(request, 'news_infos/search.html', {'inWord': inWord, 'meaningResult': meaningResult, 'keyword': keyword})

