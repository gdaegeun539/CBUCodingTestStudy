N, M = map(int, input().split())

min_card = 0

for idx in range(0, N):
  temp_min = min(list(map(int, input().split())))
  min_card = max(min_card, temp_min)

print(min_card)