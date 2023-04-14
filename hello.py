import sys
sys.stdin = open('hello.txt')
input = sys.stdin.readline
from collections import deque
from pprint import pprint


while True:
    a, b, c = map(int, input().split())

    if a == b == c == 0:
        break

    if a + b <= c or a + c <= b or b + c <= a:
        print("Invalid")
    elif a == b == c:
        print("Equilateral")
    elif a == b or b == c or c == a:
        print("Isosceles")
    else:
        print("Scalene")