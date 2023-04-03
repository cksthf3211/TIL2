import sys
# sys.stdin = open('hello.txt')
input = sys.stdin.readline
from collections import deque
from pprint import pprint


# n = list(map(int, input().split()))


while True:
    try:
        print(input())
    except EOFError:
        break
