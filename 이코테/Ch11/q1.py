n = int(input())

# 모험가들 받아서 내림차순으로 정렬
user_list = list(map(int, input().split()))
user_list.sort(reverse = True)

list_left_len = len(user_list)
group_cnt = 0

idx = 0
while idx < len(user_list):
  if user_list[idx] < list_left_len:
    group_cnt += 1
    list_left_len -= user_list[idx]
    idx += user_list[idx]
  else:
    idx += 1

print(group_cnt)