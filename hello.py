import sys
sys.stdin = open('hello.txt')
input = sys.stdin.readline
from collections import deque
from pprint import pprint


# n = list(map(int, input().split()))

c = [[] for _ in range(15)] # 2차원 배열을 만들어줌, 문자열 길이 최대 15개
# pprint(c)
# [[], [], [], [], [], [], [], [], [], [], [], [], [], [], []]

for i in range(5):         # 입력 5줄
    d = list(input().strip())      # 문자열 받아옴(공백X)
    d_len = len(d)         # 문자열의 길이
    
    for j in range(d_len): # 문자열의 길이만큼
        c[j].append(d[j])     # 2차원 배열에 문자열을 넣어줌
    # for문을 이용하여 2차원배열 [i] 입력받은 줄, [j] 문자열의 길이 = 문자열, 문자열의 길이만큼
# pprint(c)
# [['A', 'a', '0', 'a', 'P'],
#  ['A', 'f', '9', '8', '5'],
#  ['B', 'z', '1', 'E', 'h'],
#  ['C', 'z', '2', 'W', '3'],
#  ['D', '1', 'g', 'k'],
#  ['D', '6', 'x'],
#  [],
#  [],
#  [],
#  [],
#  [],
#  [],
#  [],
#  [],
#  []]
for i in range(15):        # 문자열 길이 최대 15개
    for j in range(len(c[i])): # i번째 열에 대해 존재하는 문자열만 출력
        print(c[i][j], end='')