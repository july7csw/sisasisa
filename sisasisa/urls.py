from django.urls import path
from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.hotWord, name='index'),
    path('steady', views.steadyWord, name='steady'),
    path('addSteady', views.addSteady, name='addSteady'),
    path('hot', views.hotWord, name='hot'),
    path('addHot', views.addHot, name='addHot'),
    path('myScrap', views.myScrap, name='myScrap'),
    path('search', views.search, name='search'),
    path('findMeaning', views.findMeaning, name='findMeaning'),
    path('insertScrap', views.insertScrap, name='insertScrap'),
    path('deleteScrap', views.deleteScrap, name='deleteScrap'),
    path('scrapCheck', views.scrapCheck, name='scrapCheck'),
]
