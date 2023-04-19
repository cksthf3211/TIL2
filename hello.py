import sys
sys.stdin = open('hello.txt')
input = sys.stdin.readline
from collections import deque
from pprint import pprint

n = int(input())

cnt = 0  # 고양이 수
ans = float('inf')  # 최소 행동 횟수

while True:
    # 생성 마법 사용
    cnt += 1

    # 고양이 수가 목표값과 같으면 종료
    if cnt == n:
        ans = min(ans, 1)
        break

    # 복제 마법 사용
    for i in range(1, cnt + 1):
        # i마리를 추가할 때 필요한 행동 횟수
        add_cnt = i * (i - 1) // 2 + i
        
        # 목표값보다 고양이 수가 더 많으면 종료
        if cnt + i >= n:
            ans = min(ans, cnt + 1)
            break

        # 목표값을 만들 수 있는 경우
        if cnt + add_cnt >= n:
            ans = min(ans, cnt + 1 + i)
            break

    # 최소 횟수보다 더 많이 사용한 경우 종료
    if ans <= cnt + 1:
        break

