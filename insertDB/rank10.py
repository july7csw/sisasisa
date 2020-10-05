import pandas as pd


def returnWord():
    data = pd.read_excel("insertDB/202009_rank10.xlsx")
    words = data['word']
    return words
