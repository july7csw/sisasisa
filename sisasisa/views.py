import json
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.db.models import Q
import outputFile.py.rank10 as rank
import outputFile.py.searchDB as srch
from .models import User_scrap
from .models import Words
from django.views.decorators.csrf import csrf_exempt


# Create your views here.

def index(request):
    return render(request, 'mainMenu/index.html')


def steadyWord(request):
    category = request.GET.get('category', '')
    limit = request.GET.get('limit', '')
    words = rank.returnSteadyWord(category, limit)
    return render(request, 'mainMenu/steady.html', {'words': words})


@csrf_exempt
def addSteady(request):
    category = request.POST.get('category')
    limit = request.POST.get('limit')
    words = rank.returnSteadyWord(category, limit)
    list = []
    for i in range(0, len(words)):
        list.append(words[i])
    return HttpResponse(json.dumps(list), content_type="application/json; charset=utf-8")


def hotWord(request):
    category = request.GET.get('category', '전체')
    words = rank.findHotCategory(category)
    return render(request, 'mainMenu/index.html', {'words': words, 'category': category})


@csrf_exempt
def addHot(request):
    category = request.POST.get('category')
    limit = request.POST.get('limit')
    words = rank.returnHotWord(category, limit)
    list = []
    for i in range(0, len(words)):
        list.append(words[i])
    return HttpResponse(json.dumps(list), content_type="application/json; charset=utf-8")


def checkLogin(request):
    now_user = request.user
    if now_user.is_authenticated:
        logincheck = True
    else:
        logincheck = False
    return logincheck


@csrf_exempt
def scrapCheck(request):
    msg = ""
    word = request.POST.get('word')
    user_Identifier = request.user.email
    scrapCheck = srch.findScrapList(word, user_Identifier)
    if scrapCheck is True:
        msg = 'yes'
    else:
        msg = 'no'
    data = {
        'msg': msg
    }
    return HttpResponse(json.dumps(data), content_type='application/json')


@csrf_exempt
def insertScrap(request):
    loginCheck = checkLogin(request)
    if loginCheck is True:
        word = request.POST.get('word')
        user_Identifier = request.user.email
        result = srch.findScrapList(word, user_Identifier)
        if result is True:
            msg = '이미 스크랩한 단어입니다.'
        else:
            srch.insertScrap(word, user_Identifier)
            msg = '등록 되었습니다.'
        data = {
            'msg': msg
        }
        return HttpResponse(json.dumps(data), content_type='application/json')
    else:
        return render(request, 'user/login.html')


@csrf_exempt
def deleteScrap(request):
    word = request.POST.get('word')
    user_Identifier = request.user.email
    srch.deleteScrap(word, user_Identifier)
    return redirect('myScrap')


def myScrap(request):
    logincheck = checkLogin(request)
    if logincheck is True:
        list = User_scrap.objects.filter(user_Identifier=request.user.email)
        wordIdList = [w.wordId for w in list]
        words = []
        for i in wordIdList:
            word = Words.objects.get(id=i)
            words.append(word.word)
        return render(request, 'mainMenu/myScrap.html', {'scrapList': words})
    else:
        return redirect('user/login')


def search(request):
    keyword = request.GET.get('keyword', '')
    words = Words.objects.all()

    if not keyword:
        keyword = """' '"""
        return render(request, 'mainMenu/search.html', {'notWord': keyword})
    else:
        equalWord = words.filter(word__iexact=keyword)
        inWord = words.filter(Q(word__icontains=keyword) & ~Q(word__iexact=keyword))
        inMeaning = words.filter(
            Q(meaning__icontains=keyword) & ~Q(word__icontains=keyword)
        )
        if equalWord.exists() is False and inWord.exists() is False and inMeaning.exists() is False:
            return render(request, 'mainMenu/search.html', {'notWord': keyword})
        else:
            meaningList = [im.meaning for im in inMeaning]
            inMeaning_mean = []
            for ml in meaningList:
                keywordIndex = ml.find(keyword)
                startIndex = ml[:keywordIndex].rfind(".")
                previewText = ml[startIndex + 2:]
                inMeaning_mean.append(previewText)
            inMeaning_word = [im.word for im in inMeaning]
            meaningResult = [x for x in zip(inMeaning_word, inMeaning_mean)]
            return render(request, 'mainMenu/search.html',
                          {'equalWord': equalWord,'inWord': inWord, 'meaningResult': meaningResult, 'keyword': keyword})

@csrf_exempt
def findMeaning(request):
    word = request.POST.get('word')
    wordId = srch.findWordId(word)
    meaning = srch.findMeaning(wordId)
    data = {'word': meaning}
    return HttpResponse(json.dumps(data), content_type='application/json')