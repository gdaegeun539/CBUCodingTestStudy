"""
== 백준 1647
정답처리
풀이시간 17분 46초 50
"""
from sys import stdin

input2 = stdin.readline


def find_parent(parent, x):
  if parent[x] != x:
    parent[x] = find_parent(parent, parent[x])
  return parent[x]


def union_parent(parent, x, y):
  a = find_parent(parent, x)
  b = find_parent(parent, y)

  if a < b:
    parent[b] = parent[a]
  else:
    parent[a] = parent[b]


n, m = map(int, input().split())
parent = [iter for iter in range(n + 1)]
cost_table = []
rslt_cost = []

for _ in range(m):
  start, end, cost = map(int, input2().split())
  cost_table.append((cost, start, end))

cost_table.sort()

for elem in cost_table:
  if find_parent(parent, elem[1]) == find_parent(parent, elem[2]):
    continue
  else:
    union_parent(parent, elem[1], elem[2])
    rslt_cost.append(elem[0])

rslt_cost.pop(-1)
print(sum(rslt_cost))
