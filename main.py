import sys

# def 커스텀정렬조건(val1, val2):
#   # 국어
#   if val1[1] > val2[1]:
#     return 1
#   elif val1[1] < val2[1]:
#     return -1
#   else:  # 영어
#     if val1[2] < val2[2]:
#       return 1
#     elif val1[2] > val2[2]:
#       return -1
#     else:  # 수학
#       if val1[3] > val2[3]:
#         return 1
#       elif val1[3] < val2[3]:
#         return -1
#       else:
#         return val1[0] < val1[0]

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
