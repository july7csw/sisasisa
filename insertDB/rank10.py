import pandas as pd


def returnHotWord(category):
    if len(category) == 0:
        category = '전체'
    data = pd.read_excel("insertDB/steadyRank.xlsx", sheet_name=category)
    words = data['word']
    return words


def returnSteadyWord(category):
    if len(category) == 0:
        category = '전체'
    data = pd.read_excel("insertDB/HotRank.xlsx", sheet_name=category)
    words = data['word']
    return words