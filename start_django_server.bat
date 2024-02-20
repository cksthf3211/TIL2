@echo off
cd C:\Users\sft2023\Desktop\ADR Manage\Manage
start code .
call C:/Users/sft2023/anaconda3/Scripts/activate
call conda activate Manage
@REM "Django Server"의 프롬프트에서 서버 실행
start "Django Server" python manage.py runserver

@REM 다른 프롬프트에서 해당 명령어 실행
timeout /t 3
start chrome http://127.0.0.1:8000/

@REM timeout /t 2
@REM start chrome.exe
@REM timeout /t 2
start https://papago.naver.com/

cd C:\Users\sft2023\Desktop\Messenger
start "" "뉴젠ERP.exe"

