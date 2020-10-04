from django.urls import path
from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.hot_word, name='index'),
    path('steady', views.steady, name='steady'),
    path('hot', views.hot, name='hot'),
    path('word_list', views.hot_word, name='hot_word'),
    path('scrap', views.scrap, name='scrap'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('hot', views.hot_word, name='hot'),
    path('mypage', views.mypage, name='mypage'),
]
