import os
import openpyxl
import django
import pandas as pd

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "djangoProject.settings")
django.setup()

from sisasisa.models import News_infos

writer = pd.ExcelWriter('C:/Users/myth8/PycharmProjects/django_first/insertDB/result_202001001_JUL.xlsx',
                        engine="openpyxl")

newsList = list(News_infos.objects.values())
df = pd.DataFrame(columns=['wordId', 'news_id', 'provider', 'category', 'provider_link_page', 'published_at'])

for i in range(0, len(newsList)):
    wordId = newsList[i]['wordId']
    news_id = newsList[i]['news_id']
    provider = newsList[i]['provider']
    category = newsList[i]['category']
    provider_link_page = newsList[i]['provider_link_page']
    published_at = str(newsList[i]['published_at'])
    df.loc[i] = wordId, news_id, provider, category, provider_link_page, published_at
    print(i, " / ", len(newsList))

df.to_excel(writer, sheet_name='123')
writer.save()
writer.close()