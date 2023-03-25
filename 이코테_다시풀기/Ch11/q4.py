"""
시간초과 실패
"""
from sys import stdin

input2 = stdin.readline

n = input()
coins = list(map(int, input().split()))
rslt = 0

if min(coins) != 1:
  rslt = 1
else:
  for value in range(2, max(coins)):
    # todo
    pass
    # break
  if rslt:
    rslt = max(coins) + 1

print(rslt)
