import sys


def mine(table, n, m):
  return 1


input = sys.stdin.readline

t = int(input().rstrip())
rslt = [-1] * t

for idx in range(t):
  n, m = map(int, input().rstrip().split())
  table = [[0] * m] * n
  temp_input = list(map(int, input().rstrip().split()))
  temp_idx = 0
  for row in range(n):
    for col in range(m):
      table[row][col] = temp_input[temp_idx]
      temp_idx += 1

  rslt[idx] = mine(table, n, m)

for elem in rslt:
  print(elem)
