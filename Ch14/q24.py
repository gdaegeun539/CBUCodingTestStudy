"""
== 백준 18310
1차풀이 14분 48초
1차제출 시간초과
2차풀이 포기 후 답안참조
아예 틀린풀이
"""
import sys

n = int(input())

houses = list(map(int, sys.stdin.readline().rstrip().split()))
house_sum = sum(houses)

dst = [[idx, 0] for idx in range(n)]
for idx in range(n):  # 2번돌면 최대 400억번 정도
  # for inner_idx, elem in enumerate(houses):
  #   if idx == inner_idx:
  #     continue
  #   dst[idx][1] += abs(houses[idx] - houses[inner_idx])
  dst[idx][1] = house_sum - houses[idx] * n

# 정렬 nlgn시 360만번 정도
dst.sort(key=lambda elem: (elem[1], elem[0]))

print(houses[dst[0][0]])
