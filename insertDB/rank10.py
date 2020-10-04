import pandas as pd


def returnWord():
    data = pd.read_excel("C:/Users/myth8/PycharmProjects/django_first/insertDB/202009_rank10.xlsx")
    words = data['word']
    return words
