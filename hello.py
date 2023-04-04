import sys
sys.stdin = open('hello.txt')
input = sys.stdin.readline
from collections import deque
from pprint import pprint


# n = list(map(int, input().split()))

n = int(input())
for i in range(n):
    num, s = input().split()
    text = ''
    for j in s:
        text += int(num) * j

    print(text)