from django.shortcuts import render
from .models import Words

# Create your views here.


def news_infos(request):
    return render(request, 'news_infos/index.html', {})


def word_list(request):
    words = Words.objects.all()
    return render(request, 'words/word_list.html', {'word_list': words})