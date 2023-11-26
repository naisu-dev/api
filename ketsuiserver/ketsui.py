import pandas as pd

ketsui = pd.read_csv("csv/ketsui.csv")

def number(number: int):
    try:
        number_sam = ketsui[ketsui["indexnumber"] == number]
        return [str(number_sam["roomname"].iloc[-1]),str(number_sam["ketsuimessage"].iloc[-1])]
    except:
        return "number・numberの値がおかしい可能性があります"