"""
12분 57초
"""
from sys import stdin

input2 = stdin.readline

rslt = 0
n, m = map(int, input().split())
k = list(map(int, input().split()))
k.sort()

for ball in k:
  now_ball = k.count(ball)
  k = [elem for elem in k if elem != ball]
  rslt += now_ball * len(k)

print(rslt)
