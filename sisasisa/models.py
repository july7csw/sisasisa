from django.db import models
from django.conf import settings
from django.utils import timezone


class News_infos(models.Model):
    news_id = models.CharField(max_length=100)
    provider = models.CharField(max_length=40)
    category = models.CharField(max_length=40)
    category_incident = models.CharField(max_length=40)
    provider_link_page = models.CharField(max_length=300, null=True)
    published_at = models.DateTimeField(blank=True, null=True)


class Words(models.Model):
    word = models.CharField(max_length=30)
    meaning = models.TextField()


class Assoicated_words(models.Model):
    wordId = models.CharField(max_length=30)
    word = models.CharField(max_length=30)
    weight = models.DecimalField(max_digits=5,decimal_places=2)


class Amounted_mentions(models.Model):
    wordId = models.CharField(max_length=30)
    label = models.CharField(max_length=10)
    hits = models.IntegerField()


class User_scrap(models.Model):
    user_Identifier = models.CharField(max_length=100)
    wordId = models.CharField(max_length=30)