import os
import openpyxl
import django
import pandas as pd

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "djangoProject.settings")
django.setup()

from sisasisa.models import Amounted_mentions

writer = pd.ExcelWriter('C:/Users/myth8/PycharmProjects/django_first/insertDB/result_202001001_AmountM.xlsx',
                        engine="openpyxl")

amountList = list(Amounted_mentions.objects.filter(label__startswith='2019').values())
df = pd.DataFrame(columns=['wordId', '2019'])

wordId = ''
count = 0
j = 0

for i in range(0, len(amountList)):
    wordId = amountList[i]['wordId']
    hits = amountList[i]['hits']
    count += hits
    if i+1 < len(amountList) and wordId.__ne__(amountList[i+1]['wordId']):
        df.loc[j] = wordId, count
        count = 0
        j += 1
    else:
        df.loc[j] = wordId, count
    print(i, "/", len(amountList))


print(df)

df.to_excel(writer, sheet_name='sheet1')
writer.save()
writer.close()
