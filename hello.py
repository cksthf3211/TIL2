import sys
sys.stdin = open('hello.txt')
input = sys.stdin.readline
from collections import deque
from pprint import pprint

import calendar
today = calendar.datetime.date.today()
print(calendar.month(today.year, today.month))

import datetime
now = datetime.datetime.now()
print("현재 시간은 ", now.strftime('%Y-%m-%d %H:%M'))


# n, m = map(int, input().split())
# n = list(map(int, input().split()))

import time
import winsound

# 17시59분이 되면 알람 울리기
while True:
    now = time.localtime()
    if now.tm_hour == 17 and now.tm_min == 59:
        print("알람 울립니다!")
        winsound.Beep(440, 1000) # 440 Hz 주파수로 1초 동안 소리 울리기
        break
    else:
        time.sleep(60) # 1분 대기 후 다시 검사 ctrl + c로 종료