import os
import openpyxl
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "djangoProject.settings")
django.setup()

from sisasisa.models import Words

file_PATH = 'a.xlsx'
result = []


with open(file_PATH, newline='') as files:
    wb = openpyxl.load_workbook(file_PATH)
    ws = wb.active
    print(ws)
    for r in ws.rows:
        print(r)
        Words.objects.create(
            word=r[0].value,
            meaning=r[1].value,
        )
    print("end!")

