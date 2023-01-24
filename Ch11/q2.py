input_str = input()

rslt = 0
for idx in range(len(input_str)):
  now_num = int(input_str[idx])

  # if now_num == 0 or rslt == 0:
  if now_num <= 1 or rslt <= 1:  # 1일때도 더해야 값이 커짐
    rslt += now_num
  else:
    rslt *= now_num

print(rslt)
