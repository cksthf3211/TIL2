import sys
sys.stdin = open('hello.txt')
input = sys.stdin.readline
from collections import deque
from pprint import pprint


a = int(input())
for i in range(1, a+1):
    print(i)