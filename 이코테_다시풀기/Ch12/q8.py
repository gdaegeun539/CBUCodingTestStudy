"""
8분 58초
"""
input_str = input()
rslt_char = []
rslt_sum = 0

for idx in range(len(input_str)):
  now_val = input_str[idx]
  if ord(now_val) >= 48 and ord(now_val) <= 57:
    rslt_sum += int(input_str[idx])
  else:
    rslt_char.append(now_val)

rslt_char.sort()

rslt = ""
for elem in rslt_char:
  rslt += elem

rslt += str(rslt_sum)
print(rslt)
