"""
입력예시 기준 14분 17초 (오답)
아이디어 참고해서 22분 15초
"""
import sys

guild_cnt = 0
guild = []
n = int(input())
elem = list(map(int, sys.stdin.readline().split()))

elem.sort()

idx = 0
while idx < n:
  guild.append(elem[idx])

  if max(guild) == len(guild):
    guild_cnt += 1
    guild = []

  idx += 1

print(guild_cnt)
