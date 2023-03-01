from sys import stdin

INT_INF = int(1e9)
input2 = stdin.readline

n = int(input())
m = int(input())

cost_table = [[INT_INF] * (n + 1) for _ in range(n + 1)]
for idx in range(1, n + 1):
  cost_table[idx][idx] = 0

for _ in range(m):
  row, col, temp_cost = map(int, input2().rstrip().split())
  cost_table[row][col] = min(temp_cost, cost_table[row][col])

for mid in range(1, n + 1):
  for start in range(1, n + 1):
    for end in range(1, n + 1):
      temp_cost = cost_table[start][mid] + cost_table[mid][end]
      cost_table[start][end] = min(temp_cost, cost_table[start][end])

for row in range(1, n + 1):
  for col in range(1, n + 1):
    value = cost_table[row][col] if cost_table[row][col] != INT_INF else 0
    print(value, end=" ")
  print()
