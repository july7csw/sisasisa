import json

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.db.models import Q
import insertDB.rank10 as rank
import insertDB.searchDB as srch
import insertDB.makeWordcloud as mc
from .models import User_scrap
from .models import Words
from django.views.decorators.csrf import csrf_exempt

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


def insertScrap(request):
    loginCheck = check_login(request)
    if loginCheck is True:
        word = request.GET.get('word', '')
        user_Identifier = request.user.email
        srch.insertScrap(word, user_Identifier)
        return render(request, "words/scrap.html")
    else:
        return render(request, 'member/../user/templates/user/login.html')


def scrap(request):
    logincheck = check_login(request)
    if logincheck is True:
        list = User_scrap.objects.filter(user_Identifier=request.user.email)
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


def search(request):
    keyword = request.GET.get('keyword', '')
    words = Words.objects.all()
    mc.makeWordcloud(keyword)

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
    print(word)
    wordId = srch.findWordId(word)
    meaning = srch.findMeaning(wordId)
    data = {'word': meaning}
    return HttpResponse(json.dumps(data), content_type='application/json')
