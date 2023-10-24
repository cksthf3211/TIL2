import random
import time

members = [
    'ㅇㅈㅈ 부장', 
    'ㄱㅈㄱ 사원', 
    'ㅂㅎㅈ 대리', 
    'ㅈㅇㅈ 대리', 
    'ㄱㅇㅇ 사원', 
    'ㅂㅊㅅ 사원'
    ]

menu = [
    "짜장면", 
    "짬뽕", 
    "볶음밥", 
    "불고기", 
    "김치찌개", 
    "된장찌개", 
    "초밥", 
    "피자", 
    "햄버거", 
    "샐러드",
    "돈까스"
    ]

def countdown():
    for i in range(3, 0, -1):
        print(f"{i}")
        time.sleep(1)

selected_menu = random.choice(menu)
countdown()
print(f'오늘의 점심 메뉴는 "{selected_menu}" 입니다.')

selected_member = random.choice(members)
countdown()
print(f'오늘은 {selected_member}님이 쏜다. ⎝̐̈⎛̐̈•̐̈‿̐̈•̐̈⎞̐̈⎠̐̈')
