from django.urls import path
from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.hot_word, name='index'),
    path('steady', views.steady_word, name='steady'),
    path('addSteady', views.addSteady, name='addSteady'),
    path('hot', views.hot_word, name='hot'),
    path('addHot', views.addHot, name='addHot'),
    path('myscrap', views.myscrap, name='myscrap'),
    path('search', views.search, name='search'),
    path('insertScrap', views.insertScrap, name='insertScrap'),
    path('deleteScrap', views.deleteScrap, name='deleteScrap'),
    path('findMeaning', views.findMeaning, name='findMeaning'),
    path('scrapCheck', views.scrapCheck, name='scrapCheck'),
    # path('categoryFilter', views.categoryFilter, name="categoryFilter")
]
