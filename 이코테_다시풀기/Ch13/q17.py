"""
30분 초과
"""
from collections import deque
from sys import stdin

input2 = stdin.readline

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def bfs(graph, s, q, k):
  times = 0

  while times != s:
    for idx in range(k):
      test_x, test_y = q[idx].popleft()

      for move in range(4):
        if test_x + dx[move] not in [-1, n
                                     ] and test_y + dy[move] not in [-1, n]:
          if graph[test_x + dx[move]][test_y + dy[move]] == 0:
            graph[test_x][test_y] = idx + 1
            q[idx].append((test_x + dx[move], test_y + dy[move]))


n, k = map(int, input().split())
graph = [[]] * (n)
for idx in range(n):
  tmp = list(map(int, input2().rstrip().split()))
  graph[idx] = tmp
s, x, y = map(int, input().split())
x -= 1
y -= 1

q = [deque() for _ in range(k)]

for x_idx in range(n):
  for y_idx in range(n):
    if graph[x_idx][y_idx] in range(1, k + 1):
      q[graph[x_idx][y_idx] - 1].append((x_idx, y_idx))

bfs(graph, s, q, k)

print(graph[x][y])
