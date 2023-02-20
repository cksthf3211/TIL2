import sys
input = sys.stdin.readline
from collections import deque

# n, m= map(int, input().split())
# s = input()

# ans = []

# for i in range(len(s)):
#     for j in range(i, len(s)):
#         temp = s[i:j + 1]
#         ans.append(set(temp))

# print(len(ans))

s = input()
ans = set()

for i in range(len(s)):
    for j in range(i, len(s)):
        temp = s[i:j + 1]
        ans.add(temp)

print(len(ans))