from django.urls import path
from . import views

urlpatterns = [
    path('', views.news_infos, name='news_infos'),
    path('word_list', views.word_list, name='word_list')
]
