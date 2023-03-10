import sys
sys.stdin = open('hello.txt')
input = sys.stdin.readline
from collections import deque
from pprint import pprint


# n = list(map(int, input().split()))

n, m = map(int, input().split())  # 공의 개수, 바구니의 수
basket = [0 for i in range(n)]    # 바구니 초기화
# print(basket) [0, 0, 0, 0, 0]


for i in range(m):
    a, b, c = map(int, input().split())  # a부터 b범위까지 c 번호만 넣음

    for j in range(a, b+1):       # a부터 b범위
        basket[j-1] = c           # 첫번째 바구니의 번호가 1번이고 배열의 첫번째 인덱스는 0이므로 i번째 배열의 값을 대입해주기위해  basket[j-1] = c 로 표현

# for k in basket:
#     print(k, end = ' ')
print(*basket)