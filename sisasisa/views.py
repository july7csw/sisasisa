from django.shortcuts import render

# Create your views here.

def news_infos(request):
    return render(request, 'news_infos/news_infos.html', {})
