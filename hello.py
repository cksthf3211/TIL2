import sys
sys.stdin = open('hello.txt')
input = sys.stdin.readline
from collections import deque
from pprint import pprint


color = ['black', 'brown', 'red', 'orange', 'yellow', 'green', 'blue', 'violet', 'grey', 'white']

f = color.index(input().strip())
s = color.index(input().strip())
t = color.index(input().strip())

print(int(str(f) + str(s)) * (10 ** t))