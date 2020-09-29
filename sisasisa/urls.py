from django.urls import path
from . import views

urlpatterns = [
    path('', views.hot_word, name='news_info'),
    path('word_list', views.word_list, name='word_list'),
    path('hot_word', views.hot_word, name='hot_word'),
    path('scrap', views.scrap, name='scrap'),
]
