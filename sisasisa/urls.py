from django.urls import path
from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.hot_word, name='index'),
    path('steady', views.steady_word, name='steady'),
    path('hot', views.hot_word, name='hot'),
    path('myscrap', views.myscrap, name='myscrap'),
    path('search', views.search, name='search'),
    path('insertScrap', views.insertScrap, name='insertScrap'),
    path('findMeaning', views.findMeaning, name='findMeaning'),
    path('scrapCheck', views.scrapCheck, name='scrapCheck'),
]
