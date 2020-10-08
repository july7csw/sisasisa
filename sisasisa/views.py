import json

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.db.models import Q
import insertDB.rank10 as rank
import insertDB.searchDB as srch
from .models import User_scrap
from .models import Words
from django.views.decorators.csrf import csrf_exempt


# Create your views here.

def index(request):
    return render(request, 'news_infos/index.html')


def steady_word(request):
    words = rank.returnSteadyWord()
    return render(request, 'news_infos/steady.html', {'words': words})


def hot_word(request):
    hotWords = rank.returnHotWord()
    steadyWords = rank.returnSteadyWord()
    return render(request, 'news_infos/index.html', {'steadyWords': steadyWords, 'hotWords': hotWords})


def check_login(request):
    now_user = request.user
    if now_user.is_authenticated:
        logincheck = True
    else:
        logincheck = False
    return logincheck


def detail_word(request):
    word = Words.objects.get(word=request.__getattribute__('word'))
    meaning = word.__getattribute__('meaning')
    return render(request, 'words/detail_word.html', {'word': word, 'meaning': meaning})


def login(request):
    return render(request, 'user/login.html', {})


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
    loginCheck = check_login(request)
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


def myscrap(request):
    logincheck = check_login(request)
    if logincheck is True:
        list = User_scrap.objects.filter(user_Identifier=request.user.email)
        wordIdList = [w.wordId for w in list]
        words = []
        for i in wordIdList:
            word = Words.objects.get(id=i)
            words.append(word.word)
        return render(request, 'news_infos/myscrap.html', {'scrapList': words})
    else:
        return redirect('user/login')


def login(request):
    return render(request, 'user/login.html', {})


def mypage(request):
    this_user = request.user
    message = "로그인이 필요한 페이지입니다."
    if this_user.is_authenticated:
        print(request.user.email)
        user = "user 데이터를 가져온 뒤 처리"
        return render(request, 'member/mypage.html', {'user': user})
    else:
        return redirect('user/login')


def search(request):
    print("왔니?")
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
                previewText = ml[startIndex + 2:]
                inMeaning_mean.append(previewText)
            inMeaning_word = [im.word for im in inMeaning]
            meaningResult = [x for x in zip(inMeaning_word, inMeaning_mean)]
            return render(request, 'news_infos/search.html',
                          {'inWord': inWord, 'meaningResult': meaningResult, 'keyword': keyword})


@csrf_exempt
def findMeaning(request):
    word = request.POST.get('word')
    wordId = srch.findWordId(word)
    meaning = srch.findMeaning(wordId)
    data = {'word': meaning}
    return HttpResponse(json.dumps(data), content_type='application/json')


@csrf_exempt
def deleteScrap(request):
    word = request.POST.get('word')
    user_Identifier = request.user.email
    srch.deleteScrap(word, user_Identifier)
    return redirect('myscrap')


def categoryFilter(request):
    category = request.GET.get('category', '')
    data = srch.findCategoryRank(category)
    return render(request, 'news_infos/index.html', {''})