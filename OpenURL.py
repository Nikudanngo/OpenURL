import json
import webbrowser
import datetime
from tkinter import messagebox

nowClass = 0

# 現在の時間を4桁の数字に変換
# 例：12:40→1240
now = datetime.datetime.now()  # 現在の時間を取得
dayOfWeek = now.strftime('%A')  # 曜日を取得
now_time = now.hour*100 + now.minute  # 現在の時間を4桁の数字に変換


# 現在が何時間目かを特定する関数
def WhatNowClass(now_time):
    if(now_time > 850 and now_time < 1050):
        return 1
    elif(now_time >= 1050 and now_time < 1240):
        return 2
    elif(now_time >= 1310 and now_time < 1510):
        return 3
    elif(now_time >= 1510 and now_time < 1700):
        return 4
    elif(now_time >= 1700 and now_time < 1850):
        return 5
    elif(now_time >= 1850 and now_time < 2040):
        return 6
    else:
        return 0


# ウイルスみたいなエラーを表示する
# 不要なら以下の関数を消しても問題ない
def Error():
    messagebox.showerror("error message", "授業が見つかりません")
    print("授業が見つかりません")


# json読み込み
url = open('./ClassSchedule.json', 'r', encoding="utf-8")
data = json.load(url)
# 今が何時間目なのか取得
nowClass = WhatNowClass(now_time)

# テスト
# nowClass = 1
# dayOfWeek = "Monday"

# 今が何時間目か，今日の曜日がjsonにあるか判定
if (nowClass == 0) or (dayOfWeek not in data):
    Error()
    print("授業が見つかりません")
else:
    webbrowser.open(data[str(dayOfWeek)][str(nowClass)]["url"])
    print(data[str(dayOfWeek)][str(nowClass)]["class"])
