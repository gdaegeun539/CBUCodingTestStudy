"""
5분 43초
"""
input_str = input()
mid = len(input_str) // 2
rslt = 0

for idx in range(mid):
  rslt += int(input_str[idx])
for idx in range(mid, len(input_str)):
  rslt -= int(input_str[idx])

if not rslt:
  print("LUCKY")
else:
  print("READY")
