import sys
sys.stdin = open('hello.txt')
input = sys.stdin.readline
from collections import deque
from pprint import pprint

# import calendar
# today = calendar.datetime.date.today()
# print(calendar.month(today.year, today.month))

# import datetime
# now = datetime.datetime.now()
# print("현재 시간은 ", now.strftime('%Y-%m-%d %H:%M'))


# n, m = map(int, input().split())
# n = list(map(int, input().split()))


import calendar
import datetime
import time
import webbrowser
import os

today = calendar.datetime.date.today()
print(calendar.month(today.year, today.month))

now = datetime.datetime.now()
print("현재 시간은 ", now.strftime('%Y-%m-%d %H:%M'))

while True:
    now = time.localtime()
    if now.tm_hour == 17 and now.tm_min == 59:
        print("알람 울립니다!")
        url = "https://youtu.be/xbO1CY1PXkE"
        webbrowser.open(url)
        time.sleep(30)
        os.system("taskkill /im chrome.exe /f")
        time.sleep(60)                                 # 1분 대기
        print("마지막 알람입니다!")
        url = "https://youtu.be/xbO1CY1PXkE"
        webbrowser.open(url)
        now = datetime.datetime.now()
        print("현재 시간은 ", now.strftime('%Y-%m-%d %H:%M'))
        time.sleep(30)
        print("시스템 종료합니다!")
        os.system('taskkill /f /im explorer.exe')      # 시스템 종료
        os.system('taskkill /f /im MicrosoftEdge.exe') # 시스템 종료
        os.system('taskkill /f /im chrome.exe')        # 시스템 종료
        print("30초 후 컴퓨터 종료합니다!")
        print("현재 시간은 ", now.strftime('%Y-%m-%d %H:%M'), "오늘도 고생하셨습니다.")
        cnt = 0
        while cnt < 60:
            cnt += 1
            time.sleep(1)
            print(cnt)

            os.system('shutdown /s /t 0')              # 컴퓨터 종료
