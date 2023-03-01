"""
시간초과
접근 틀림
"""
import heapq
INT_INF = int(1e9)

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
cost = [[INT_INF] * (n + 1) for _ in range(n+1)]
# directed_cnt = [0] * (n + 1)

for _ in range(m):
  node, dst = map(int, input().split())
  graph[node].append(dst)

for idx in range(n):
  graph[idx].sort()

for node in range(1, n+1):
  if graph[node]:
    que = []
    heapq.heappush(que, (0, node))
    while que:
      dist, now_node = heapq.heappop(que)
      if cost[node][now_node] < dist:
        continue
      else:
        cost[node][now_node] = dist
        for edge in graph[now_node]:
          heapq.heappush(que, (dist + 1, edge))

cnt = [0] * n+1
for col in range(1, n+1):
  # cnt[col] = 0
  for row in range(1, n+1):
    if row == col:
      continue
    cnt[col] += cost[row][col]

rslt = 0
for node in range(1, n + 1):
  if len(graph[node]) + cnt[node] == n-1:
    rslt += 1

print(rslt)