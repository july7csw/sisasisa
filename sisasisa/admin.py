from django.contrib import admin
from .models import News_infos
from .models import Words
from .models import Assoicated_words
from .models import Amounted_mentions
from .models import User_scrap

admin.site.register(News_infos)
admin.site.register(Words)
admin.site.register(Assoicated_words)
admin.site.register(Amounted_mentions)
admin.site.register(User_scrap)
