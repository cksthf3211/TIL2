import sys
sys.stdin = open('hello.txt')
input = sys.stdin.readline
from collections import deque
from pprint import pprint

# n바구니, m번 공 바꾸기
n, m = map(int, input().split())

box = [i for i in range(1, n+1)]
# print(box) [1, 2, 3, 4, 5] 공을 담을 박스 만듦

for i in range(m):
    i, j = map(int, input().split())
    temp = box[i-1]
    # print(temp) 1 3 2 1 박스에 공을 넣음음
    box[i-1] = box[j - 1]
    box[j - 1] = temp
for j in box: # [3, 1, 4, 2, 5]
    print(j, end=" ")