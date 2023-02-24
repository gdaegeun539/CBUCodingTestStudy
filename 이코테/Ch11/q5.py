# 잘못된 접근인듯? (n 미사용)

n, m = list(map(int, input().split()))

ball_list = list(map(int, input().split()))

result = 0

for a_select in range(1, m + 1):
  cp_list = ball_list.copy()
  print(f"before: {cp_list}")
  while a_select in cp_list:
    cp_list.remove(a_select)
  result += len(cp_list)
  print(f"after: {cp_list}")

print(result)
