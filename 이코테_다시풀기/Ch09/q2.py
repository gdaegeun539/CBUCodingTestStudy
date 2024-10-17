import sys

input2 = sys.stdin.readline

INT_INF = int(1e9)

n, m = map(int, input2().split())
graph = [[INT_INF for _ in range(n)] for _ in range(n)]

for idx in range(n):
  graph[idx][idx] = 0

for _ in range(m):
  a, b = map(int, input2().split())
  graph[a - 1][b - 1] = 1
  graph[b - 1][a - 1] = 1

x, k = map(int, input2().split())

for 중간점 in range(n):
  for 시작점 in range(n):
    for 끝점 in range(n):
      graph[시작점][끝점] = min(graph[시작점][끝점], (graph[시작점][중간점] + graph[중간점][끝점]))

if graph[0][k - 1] == INT_INF or graph[k - 1][x - 1] == INT_INF:
  print(-1)
else:
  print(graph[0][k - 1] + graph[k - 1][x - 1])
