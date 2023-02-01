# 아이디어는 동일하나 순회시 원소 누락 버그가 있음
data = list(input())
sum = 0

for dat in data:
  print(dat)
  if dat.isdigit():
    print(f"debug>>> sum_dat: {dat}")
    sum += int(dat)
    data.remove(dat)
  else:
    print(f"Debug>>> {dat}")

print(data)
rslt_str = "".join(sorted(data))

print(f"rslt_str: {rslt_str}")
print(f"sum: {sum}")
