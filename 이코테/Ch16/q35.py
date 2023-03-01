"""
19분 50초
"""
n = int(input())

set_235 = set([1, 2, 3, 5])
idx = 1
while len(set_235) < n * 2:
  list_235 = list(set_235)
  list_235.append(list_235[idx] * 2)
  list_235.append(list_235[idx] * 3)
  list_235.append(list_235[idx] * 5)
  set_235 = set(list_235)
  # print(len(set_235))
  idx += 1

# print(set_235)
print(list(set_235)[n - 1])
