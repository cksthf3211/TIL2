import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
n_list = sorted(list(map(int, input().split())))
x = int(input())

left, right = 0, n-1
cnt = 0

# print(n)
# print(n_list)
# print(x)
# 9
# [1, 2, 3, 5, 7, 9, 10, 11, 12]
# 13

while left < right: # 왼쪽, 오른쪽 방향의 인덱스가 서로 만날 때(교차할 때)까지 진행
    # 두 수의 합이 x보다 큰 경우 - 더 큰 값을 더해야하므로 left+1
    # 두 수의 합이 x보다 작은 경우 - 더 작은 값을 더해야하므로 right-1
    # 두 수의 합이 x인 경우 - answer+1 & left+1
    temp = n_list[left] + n_list[right]
    if temp == x:
        cnt += 1
        left += 1
    elif temp < x:
        left += 1
    else:
        right -= 1

print(cnt)