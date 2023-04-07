import sys
sys.stdin = open('hello.txt')
input = sys.stdin.readline
from collections import deque
from pprint import pprint



# 무한히 반복하며 사용자로부터 입력을 받음
while True:
    try:
        # 사용자로부터 두 개의 정수를 입력받음
        x, y = map(int, input().split())

        # 현재까지의 승률을 계산
        win_rate = y * 100 // x

        # 현재까지의 승률이 99% 이상이면 -1을 출력하고 다음 반복으로 넘어감
        if win_rate >= 99:
            print("-1")
            continue

        # 이진 탐색을 이용하여 최소 게임 횟수를 찾음
        left, right = 0, 1000000000
        while left <= right:
            mid = (left + right) // 2
            temp_win_rate = (y + mid) * 100 // (x + mid)
            if temp_win_rate > win_rate:
                right = mid - 1
            else:
                left = mid + 1

        # 최소 게임 횟수를 출력함
        print(left)

    # 예외가 발생하면 반복문을 탈출함
    except:
        break


while True:
    try:
        x, y = map(int, input().split())

        win_rate = y * 100 // x

        if win_rate >= 99:
            print("-1")
            continue

        # 최소 게임 횟수를 찾는 것이 목적이므로
        # left, right, mid 모두 게임 횟수로 설정
        left, right = 1, 1000000000
        while left <= right:
            mid = (left + right) // 2
            temp_win_rate = (y + mid) * 100 // (x + mid)
            if temp_win_rate <= win_rate:
                left = mid + 1
            else:
                right = mid - 1

        print(left)

    except:
        break
