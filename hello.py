import sys
sys.stdin = open('hello.txt')
input = sys.stdin.readline
from collections import deque
from pprint import pprint


# 입력
current_time = list(map(int, input().split(':')))
start_time = list(map(int, input().split(':')))

# 필요한 시간
current_sec = current_time[0]*3600 + current_time[1]*60 + current_time[2]
start_sec = start_time[0]*3600 + start_time[1]*60 + start_time[2]
res = start_sec - current_sec

# 만약 다음날이면 하루만큼 시간 더해주기
if res < 0:
    res += 24*3600

# 시간 환산 후 출력
print(f"{res//3600:02d}:{(res%3600)//60:02d}:{res%60:02d}")