# QDate 클래스는 날짜와 관련된 기능들을 제공
from PyQt5.QtCore import QDate

now = QDate.currentDate()   # currentDate() 메서드는 현재 날짜를 반환
print(now.toString())       # toString() 메서드를 통해 현재 날짜를 문자열로 출력
# 수 4 12 2023

from PyQt5.QtCore import QDate, Qt

now = QDate.currentDate()
print(now.toString('d.M.yy'))                 # 12.4.23
print(now.toString('dd.MM.yyyy'))             # 12.04.2023
print(now.toString('ddd.MMMM.yyyy'))          # 수.4월.2023
print(now.toString(Qt.ISODate))               # 2023-04-12
print(now.toString(Qt.DefaultLocaleLongDate)) # 2023년 4월 12일 수요일
# Qt.ISODate, Qt.DefaultLocaleLongDate를 입력함으로써 ISO 표준 형식 또는 어플리케이션의 기본 설정에 맞게 출력

# QTime 클래스를 사용해서 현재 시간을 출력
from PyQt5.QtCore import QTime

time = QTime.currentTime()  # currentDateTime() 메서드는 현재의 날짜와 시간을 반환
print(time.toString())      # toString() 메서드는 날짜와 시간을 문자열 형태로 반환
# 10:21:07

from PyQt5.QtCore import QTime, Qt

time = QTime.currentTime()
print(time.toString('h.m.s'))                  # 10.21.7
print(time.toString('hh.mm.ss'))               # 10.21.07
print(time.toString('hh.mm.ss.zzz'))           # 10.21.07.336
print(time.toString(Qt.DefaultLocaleLongDate)) # 오전 10:21:07
print(time.toString(Qt.DefaultLocaleShortDate))# 오전 10:20
# Qt.DefaultLocaleLongDate 또는 Qt.DefaultLocaleShortDate 등으로 시간의 형식을 설정


from PyQt5.QtCore import QDateTime, Qt

datetime = QDateTime.currentDateTime()
print(datetime.toString('d.M.yy hh:mm:ss'))         # 12.4.23 10:25:18
print(datetime.toString('dd.MM.yyyy, hh:mm:ss'))    # 12.04.2023, 10:25:18
print(datetime.toString(Qt.DefaultLocaleLongDate))  # 2023년 4월 12일 수요일 오전 10:25:18
print(datetime.toString(Qt.DefaultLocaleShortDate)) # 2023-04-12 오전 10:25
# Qt.DefaultLocaleLongDate 또는 Qt.DefaultLocaleShortDate를 입력