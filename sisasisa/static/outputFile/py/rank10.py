import json
import pandas as pd


def returnHotWord(category, limit):

    if limit is None or len(limit) == 0:
        limit = 10
    else:
        limit = int(limit)
    if category is None or len(category) == 0:
        category = '전체'
    data = pd.read_excel("/static/outputFile/xlsx/hotWordData.xlsx", sheet_name=category)
    words = data['word'].head(limit)
    return words


def returnSteadyWord(category, limit):
    if limit is None or len(limit) == 0:
        limit = 10
    else:
        limit = int(limit)
    if category is None or len(category) == 0:
        category = '전체'
    data = pd.read_excel("/static/outputFile/xlsx/steadyRank.xlsx", sheet_name=category)
    words = data['word'].head(limit)
    return words


def findHotCategory(category):
    data = pd.read_excel("/static/outputFile/xlsx/hotWordData.xlsx", sheet_name=category)
    words = data['word'][1:11]
    return words