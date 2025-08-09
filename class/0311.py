import keyword
print(keyword.kwlist) # 파이썬에서 사용할 수 없는 키워드 보기!

import calendar
print(calendar.month(2025, 1)) # 2025년 1월의 달력은...

import datetime
now = datetime.datetime.now()
print(now.year, now.month, now.day, now.hour, now.minute, now.second) # 몇년 몇월 몇일 몇시 몇분 몇초

# import tkinter as tk
# base = tk.Tk() # GUI 만들기!

import turtle as t # 거북이 소환!
t.shape("turtle")
t.forward(100)
t.left(145)
t.forward(100)
t.left(145)
t.forward(100)
t.left(145)
t.forward(100)
t.left(145)
t.forward(200)
t.left(145)
t.forward(100)
t.left(145)
t.forward(100)
t.left(145)
t.forward(100)
t.left(145)
t.forward(100)
t.exitonclick()