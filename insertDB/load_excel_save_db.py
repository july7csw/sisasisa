import os
import csv
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "djangoProject.settings")
django.setup()

from sisasisa.models import Amounted_mentions

file_PATH = 'a.csv'
result = []

with open(file_PATH, newline='') as file:
    data_reader = csv.DictReader(file)
    for r in data_reader:
        print(r)
        Amounted_mentions.objects.create(
            wordId= r['1'],
            label='202008',
            hits=r['202008']
        )
    print("end!")