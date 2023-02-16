import sys
input = sys.stdin.readline
from collections import deque

n, m= map(int, input().split())
n_list = []

# 재귀함수 이용
def dfs():
    if len(n_list) == m:
        print(' '.join(map(str, n_list)))
        return
    
    for i in range(1, n+1):
        if i not in n_list:
            n_list.append(i)
            dfs()
            n_list.pop()

dfs()