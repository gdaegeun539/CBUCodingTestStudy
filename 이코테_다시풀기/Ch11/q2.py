"""
5분 38초
"""
s = input()

rslt_sum = 0

for idx in range(len(s)):
  now_num = int(s[idx])
  if rslt_sum <= 1 or now_num <= 1:
    rslt_sum += now_num
  else:
    rslt_sum *= now_num

print(rslt_sum)
