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
# graph = [[] for _ in range(n+1)]
parent = [idx for idx in range(n + 1)]

for _ in range(m):
  oper, a, b = map(int, input2().split())
  if oper == 0:
    union_parent(parent, a, b)
  else:
    rslt = "NO"
    if find_parent(parent, a) == find_parent(parent, b):
      rslt = "YES"
    print(rslt)
