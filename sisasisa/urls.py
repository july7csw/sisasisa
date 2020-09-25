from django.urls import path
from . import views

urlpatterns = [
    path('', views.news_infos, name='news_infos'),
]