N, M = map(int, input().split())

min_card = 0

for idx in range(0, N):
  temp_list = sorted(list(map(int, input().split())))
  if min_card < temp_list[0]:
    min_card = temp_list[0]

print(min_card)