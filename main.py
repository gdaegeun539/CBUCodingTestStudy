from collections import deque
from sys import stdin

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

input2 = stdin.readline

n, k = map(int, input2().rstrip().split())
graph = []

for _ in range(n):
    graph.append(list(input2().rstrip().split()))

s, x, y = map(int, input2().rstrip().split())

def bfs():
    q = deque([])
    
    for i in range(n):
        for j in range(n):
            if graph[i][j] != 0:
                q.append((graph[i][j], i, j))

    q.sort()
    
    while q:
        node, x, y = q.popleft()

        for idx in range(4):
            movx = x + dx[idx]
            movy = y + dy[idx]

            if movx < 0 or movx >= n or movy < 0 or movy >= n:
                continue

            if graph[movx][movy] == 0:
                graph[movx][movy] = node
                q.append((node, movx, movy))

bfs()

print(graph[x-1][y-1])