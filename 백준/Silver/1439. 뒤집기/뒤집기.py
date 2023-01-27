dasom_num = input()

start_num = dasom_num[0]
check_num = ""
rslt_cnt = 0

for idx in range(1, len(dasom_num)):
  if dasom_num[idx] != start_num:
    if check_num == "":
      rslt_cnt += 1
      check_num = dasom_num[idx]
  else:
    if check_num != dasom_num[idx]:
      check_num = ""

print(rslt_cnt)
