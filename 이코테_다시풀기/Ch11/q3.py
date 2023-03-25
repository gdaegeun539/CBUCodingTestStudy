"""
10분 30초
채점통과 / 31256KB, 40ms
"""
s = input()

rslt = 0
first_char = s[0]
is_reverse = False

for idx in range(1, len(s)):
  if s[idx] != first_char:
    is_reverse = True
  else:
    if is_reverse:
      rslt += 1
      is_reverse = False
    continue

if is_reverse:
  rslt += 1

print(rslt)