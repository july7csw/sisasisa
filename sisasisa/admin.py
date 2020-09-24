from django.contrib import admin
from .models import news_infos
from .models import words
from .models import assoicated_words
from .models import amounted_mentions
from .models import user_scrap

admin.site.register(news_infos)
admin.site.register(words)
admin.site.register(assoicated_words)
admin.site.register(amounted_mentions)
admin.site.register(user_scrap)
