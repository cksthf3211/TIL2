import sys
sys.stdin = open('hello.txt')
input = sys.stdin.readline
from collections import deque
from pprint import pprint


n = input().split('-')
# ['55', '50+40']

num = 0
for i in n[0].split('+'):
    # print(i)
    # 55
    num += int(i)

for j in n[1:]:
    # print(j)
    # 50+40
    for k in j.split('+'):
        num -= int(k)
        # print(k)
        # 50
        # 40
print(num)
