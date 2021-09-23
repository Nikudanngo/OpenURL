from tkinter.constants import CASCADE, COMMAND
import webbrowser
import datetime
from tkinter import messagebox
import sys
import subprocess  

def WhatDay():#ここで曜日を数値に変換
    Day = ["Monday","Tuesday","Wednesday","Thursday","Friday"]
    return Day.index(dow)

def openURL(ClassTime,day_to_today_num):
    if ClassTime[day_to_today_num] != '':
        webbrowser.open(ClassTime[day_to_today_num])
        return 0
    else:
        return 1

def Error(ErrorPoint):
    if(ErrorPoint > 0):
        messagebox.showerror("error message", "授業が見つかりません")
        print("It's not class now")
n = 0
ep = 0
now = datetime.datetime.now()

# ここに時間割を入力してください。
#       　月 火 水 木 金
first = ['','','','','']
second= ['','','','','']
third = ['','','','','']
fourth= ['','','','','']
fifth = ['','','','','']
# 基礎機械学 https://us02web.zoom.us/j/83854424097?pwd=476334 or ?OTA4S0hoQ2ZXZEhPYU9DRGR4eTZPQT09
# 確率統計学　https://classroom.google.com/c/Mzg4NzE2NzEzOTQ3?cjc=lxvrhj3
# ディジタル電子回路 https://stream.meet.google.com/stream/1891a9ff-69e4-4abb-afb2-4cf0ccc20a56
# 美術史 https://drive.google.com/file/d/1d87obK-rNvet1Dvx5UGtDrUc4NBdoSqr/view?usp=sharing

dow = now.strftime('%A')
now_time = now.hour*100 + now.minute


n = WhatDay()

if(now_time > 845 and now_time < 1050):
    ep = openURL(first,n)

elif(now_time >= 1050 and now_time < 1240):
    ep = openURL(second,n)

elif(now_time >= 1310 and now_time < 1510):
    ep = openURL(third,n)

elif(now_time >= 1510 and now_time < 1700):
    ep = openURL(fourth,n)

elif(now_time >= 1700 and now_time < 1850):
    ep = openURL(fifth,n)
else:
    ep += 1

Error(ep)
    

