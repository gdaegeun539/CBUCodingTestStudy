from collections import deque
from sys import stdin

input2 = stdin.readline


def dfs(start, graph, visited):
    if not visited[start]:
        visited[start] = True
        print(start, end=" ")

        for elem in graph[start]:
            dfs(elem, graph, visited)


def bfs(start, graph, visited):
    que = deque([])
    que.append(start)

    while que:
        elem = que.popleft()
        if not visited[elem]:
            print(elem, end=" ")
            visited[elem] = True
            for next in graph[elem]:
                que.append(next)


n, m, v = map(int, input2().rstrip().split())

graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)
for _ in range(m):
    a, b = map(int, input2().rstrip().split())
    graph[a].append(b)
    graph[b].append(a)

for idx in range(n + 1):
    graph[idx].sort()

dfs(v, graph, visited)
print()
visited = [False] * (n+1)
bfs(v, graph, visited)
