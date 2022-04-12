# オンライン授業にスムーズに参加する
## 使いかた
- ClassSchedule.jsonに自分の時間割とURLを書き込む．
- 授業10分前にOpenURL.pyを実行する．

## 動作結果
OpenURL.pyを実行すると，実行した時間が授業の10分前であれば,
教室の場所とオンラン授業のURLを開いてくれます．
または，OpenURL-notifyON.pyを実行するとLINE Notifyを利用して通知を送ることもできます．

## 補足
授業時間を変更したいときはOpenURL.pyの条件if内の3~4桁の数字を変更してください.  

``` python
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
    else:
        return 0
```

例:1限目開始が9:10であれば10分前(1,3限目は20分前)から授業に入るために以下のようにしています．
|  時限目   |  開始時間  |  数字  |
|  :----:   |   :----:   | :----: |
|    1      |     9:10   |  850   |
|    2      |    11:00   |  1050  |
|    3      |    13:30   |  1310  |
|    4      |    15:20   |  1510  | 

_上記の方法で開始時間の数字を変更した場合，授業の終了時間と次の授業の開始時間がifの条件で重複しないようにして下さい．_

## 使用したライブラリやAPI
- requests
- tkinter
- notify-on
- LINE Notify API