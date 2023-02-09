import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())
string = [list(map(str, input().strip())) for _ in range(n)]
paint = []

# print(string)
# [['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
#  ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
#  ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
#  ['B', 'W', 'B', 'B', 'B', 'W', 'B', 'W'], 
#  ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
#  ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
#  ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
#  ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W']]

# 반복문을 통해 체스판을 확인(8*8 범위로 자름)
for i in range(n-7):
    for j in range(m-7):
        w = 0
        b = 0

        # 8*8 체스판 확인
        for k in range(i, i+8):
            for l in range(j, j+8):
                if (l + k) % 2 == 0: # 짝수
                    if string[k][l] != 'W':
                        w += 1
                    else:
                        b += 1
                else:
                    if string[k][l] != 'B':
                        w += 1
                    else:
                        b += 1

        paint.append(w)
        paint.append(b)

# 칠한 색 중에 최솟값
print(min(paint))