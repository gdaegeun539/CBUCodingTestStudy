"""
틀린 풀이(플로이드-워셜이 아닌 다익스트라 접근)
"""
from sys import stdin
import heapq

input = stdin.readline

n, m = map(int, input().split())
dst_list = [[int(1e9) for _ in range(n + 1)] for _ in range(2)]
graph = [[] for _ in range(n + 1)]

for _ in range(m):
  idx, dst_comp = map(int, input().split())
  graph[idx].append((1, dst_comp))  # 비용, 노드 순

end, mid = map(int, input().split())


def 다익스트라(start, end, dst_list, graph):
  queue = []

  heapq.heappush(queue, (0, start))
  dst_list[start] = 0

  while queue:
    dist, comp = heapq.heappop(queue)
    if dst_list[comp] < dist:
      continue

    for elem in graph[comp]:
      temp_dist = dist + 1
      if temp_dist < dst_list[elem[1]]:
        dst_list[elem[1]] = temp_dist
        heapq.heappush(queue, (temp_dist, elem[1]))

    if comp == end:
      break


다익스트라(1, mid, dst_list[0], graph)
다익스트라(mid, end, dst_list[1], graph)
if dst_list[0][mid] == int(1e9) or dst_list[1][end] == int(1e9):
  print(-1)
else:
  print(dst_list[0][mid] + dst_list[1][end])
