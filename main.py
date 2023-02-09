n, m, k, x = map(int, list(input().split()))

# global graph
graph = [[]] * (n + 1)
print(graph)

for loop in range(m):
  st_node, fn_node = map(int, list(input().split()))
  graph[st_node].append(fn_node)

# global lgth
lgth = [300001] * (n + 1)
lgth[x] = 0


def dfs(node, last_node, graph, lgth):
  # global lgth
  # global graph

  if node != last_node:
    test_lgth = lgth[last_node] + 1
    if test_lgth < lgth[node]:
      lgth[node] = test_lgth
    else:
      return

  for new_node in graph[node]:
    dfs(new_node, node, graph, lgth)

dfs(x, x, graph, lgth)

rslt = []
for idx, elem in enumerate(lgth[1:]):
  if elem == k:
    rslt.append(idx + 1)

if len(rslt) == 0:
  print(-1)
else:
  for elem in rslt:
    print(f"{elem}")

