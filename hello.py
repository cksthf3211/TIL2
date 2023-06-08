import sys
sys.stdin = open('hello.txt')
input = sys.stdin.readline
from collections import deque
from pprint import pprint


while True:
    name, age, weigt = input().split()
    if '#' in name:
        break
    if int(age) > 17 or int(weigt) >= 80:
        print(f"{name} Senior")
    else:
        print(f"{name} Junior")