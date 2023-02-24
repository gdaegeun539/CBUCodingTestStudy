import sys, heapq

INT_INF = int(1e9)
input = sys.stdin.readline

n, m, c = map(int, input().split())
graph = [[] for _ in range(n + 1)]
dist_list = [INT_INF for _ in range(n + 1)]

for _ in range(m):
  x, y, z = map(int, input().split())
  graph[x].append((z, y))  # 거리, 도시번호 순


def 다익스트라(start, graph, dist_list):
  que = []

  heapq.heappush(que, (0, start))
  while que:
    now_node = heapq.heappop(que)

    if now_node[0] > dist_list[now_node[1]]:
      continue

    dist_list[now_node[1]] = now_node[0]
    for test_node in graph[now_node[1]]:
      new_dist = now_node[0] + test_node[0]
      if new_dist < dist_list[test_node[1]]:
        dist_list[test_node[1]] = new_dist
        heapq.heappush(que, (new_dist, test_node[1]))


다익스트라(c, graph, dist_list)

recv_cnt = 0
now_max = -1
for idx, elem in enumerate(dist_list):
  if elem >= INT_INF or elem <= 0:
    continue
  else:
    recv_cnt += 1
    if now_max < elem:
      now_max = elem

print(recv_cnt, now_max)
