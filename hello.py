import sys
#sys.stdin = open('hello.txt')
input = sys.stdin.readline
from collections import deque
import pprint

# n, m= map(int, input().split())
n = list(map(int, input().split()))
print(sum(n)) 
