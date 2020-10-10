import pandas as pd

def returnHotWord():
    data = pd.read_excel("insertDB/202009_rank10.xlsx")
    words = data['word']
    return words


def returnSteadyWord():
    data = pd.read_excel("insertDB/202009_steady10.xlsx")
    words = data['word']
    return words