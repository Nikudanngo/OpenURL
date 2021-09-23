import json
import webbrowser
import datetime
from tkinter import messagebox

n = 0

# 現在の時間を4桁の数字に変換
# 例：12:40→1240
now = datetime.datetime.now()   
dow = now.strftime('%A')
now_time = now.hour*100 + now.minute

#現在が何時間目かを特定する関数
def WhatNowClass(now_time):
    if(now_time > 845 and now_time < 1050):
        return 1
    elif(now_time >= 1050 and now_time < 1240):
        return 2
    elif(now_time >= 1310 and now_time < 1510):
        return 3
    elif(now_time >= 1510 and now_time < 1700):
        return 4
    elif(now_time >= 1700 and now_time < 1850):
        return 5
    else:
        return 0
# ウイルスみたいなエラーを表示する
# 不要なら以下の関数を消しても問題ない
def Error():
    messagebox.showerror("error message", "授業が見つかりません")
    print("You don't have Class-Shedule!")

# json読み込み
url = open('./ClassSchedule.json','r') 
data = json.load(url)
# 今が何時間目なのか取得
n = WhatNowClass(now_time)  

# テスト
# n = 1
# dow = "Monday"

if (n == 0):
    Error()
else:
    webbrowser.open(data[str(dow)][str(n)]["url"])

