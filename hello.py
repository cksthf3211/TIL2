import sys
input = sys.stdin.readline
from collections import deque

n, k = map(int, input().split()) # n: 수빈 k: 동생
graph = [0] * 100001

def bfs():
    queue = deque([n])

    while queue:
        x = queue.popleft()

        if x == k: # 위치가 같다면
            print(graph[x]) # 그 위치를 출력
            break
        
        for i in (x - 1, x + 1, x * 2):

            if 0 <= i <= 100000 and graph[i] == 0:
                graph[i] = graph[x] + 1
                queue.append(i)
bfs()