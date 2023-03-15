import sys
sys.stdin = open('hello.txt')
input = sys.stdin.readline
from collections import deque
from pprint import pprint


# n = list(map(int, input().split()))

for _ in range(int(input())):
    A, B = map(int, input().split())
    print("yes")