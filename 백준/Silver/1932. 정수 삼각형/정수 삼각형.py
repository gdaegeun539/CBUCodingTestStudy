import sys

input2 = sys.stdin.readline
n = int(input())
triangle = [[0] * n for _ in range(n)]

for row in range(n):
  tmp = list(map(int, input2().rstrip().split()))
  tmp_idx = 0
  for col in range(len(tmp)):
    triangle[row][col] = tmp[tmp_idx]
    tmp_idx += 1

for row in range(1, n):
  for col in range(len(triangle[row])):
    if col == 0:
      triangle[row][col] = triangle[row][col] + triangle[row - 1][col]
    else:
      triangle[row][col] = triangle[row][col] + max(triangle[row - 1][col - 1], triangle[row - 1][col])

rslt = int(-1e9)
for elem in triangle[n - 1]:
  rslt = max(rslt, elem)
print(rslt)
