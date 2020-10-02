import os
import csv
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "djangoProject.settings")
django.setup()

from sisasisa.models import Amounted_mentions

file_PATH = 'aa.csv'
dic = {}

with open(file_PATH, newline='') as file:
    data_reader = csv.DictReader(file)
    for r in data_reader:
        dic = r.items()
        wordId = r['1']
        for key, value in dic:
            label = key
            hits = value
            if not key.__eq__('1'):
                Amounted_mentions.objects.create(
                    wordId=wordId,
                    label=label,
                    hits=hits
                )
    print("end!")
