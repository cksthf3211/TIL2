import sys
sys.stdin = open('hello.txt')
input = sys.stdin.readline
from collections import deque
import pprint

# n, m= map(int, input().split())
n = int(input())
p = list(map(int, input().split()))

cnt = 0
p.sort() # 오름차순 정렬
# print(p)  [1, 2, 3, 3, 4]

for i in range(n):
    for j in range(i+1): 
        cnt += p[j]
        # print(j)
        # 0
        # 0 1
        # 0 1 2
        # 0 1 2 3
        # 0 1 2 3 4

        # print(p[j])
        # 1
        # 1 2
        # 1 2 3
        # 1 2 3 3 
        # 1 2 3 3 4
        # sum = 32
print(cnt)