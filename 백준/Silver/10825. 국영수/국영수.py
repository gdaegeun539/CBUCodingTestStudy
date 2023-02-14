import sys

n = int(input())

학생들 = []
for _ in range(n):
  temp_list = list(sys.stdin.readline().rstrip().split())
  for idx in range(1, 4):
    temp_list[idx] = int(temp_list[idx])
  학생들.append(tuple(temp_list))

학생들.sort(key=lambda x: (-x[1], x[2], -x[3], x[0]))

for 학생 in 학생들:
  print(학생[0])
