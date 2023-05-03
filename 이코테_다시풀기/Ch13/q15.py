"""
시간초과, 오답
"""
from collections import deque

MAX_DIST = 300001
#n: 도시 수, m: 단방향 도로 수, x: 출발 도시, k: 최단 거리
n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n + 1)]
dist = [MAX_DIST] * (n + 1)

for _ in range(m):
  a, b = map(int, input().split())
  graph[a].append(b)


def bfs(graph, start_node, parent_node):
  que = deque()
  que.append((start_node, parent_node))

  while que:
    now_node, parent_node = que.popleft()

    if dist[now_node] + 1 > k:
      continue

    if dist[now_node] > dist[parent_node] + 1 or now_node == x:
      dist[now_node] = dist[parent_node] + 1
      for node in graph[now_node]:
        que.append((node, now_node))


bfs(graph, x, x - 1)

cnt = False
for idx, elem in enumerate(dist):
  if elem == k:
    cnt = True
    print(idx)

if not cnt:
  print(-1)
