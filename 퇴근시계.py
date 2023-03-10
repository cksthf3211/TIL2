import calendar
import datetime
import time
import webbrowser
import os

today = calendar.datetime.date.today()
print(calendar.month(today.year, today.month))

now = datetime.datetime.now()
print("현재 시간은", now.strftime('%Y-%m-%d %H:%M'), '입니다.')

while True:
    now = time.localtime()
    if now.tm_hour == 18 and now.tm_min == 2:
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
        print("현재 시간은", now.strftime('%Y-%m-%d %H:%M'), '입니다.')
        time.sleep(30)
        print("시스템 종료합니다!")
        os.system('taskkill /f /im explorer.exe')      # 시스템 종료
        os.system('taskkill /f /im MicrosoftEdge.exe') # 시스템 종료
        os.system('taskkill /f /im chrome.exe')        # 시스템 종료
        print("30초 후 컴퓨터 종료합니다!")
        print("현재 시간은", now.strftime('%Y-%m-%d %H:%M'), "오늘도 고생하셨습니다.")
        cnt = 30
        while cnt >= 0:
            cnt -= 1
            time.sleep(1)
            print(cnt,'초 후 컴퓨터를 종료합니다.')
            if cnt == 0:
                os.system('shutdown /s /t 0')              # 컴퓨터 종료