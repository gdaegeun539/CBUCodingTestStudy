data = input()
left_idx = len(data) // 2 - 1

left_sum = 0
right_sum = 0

for idx in range(0, left_idx + 1):
  dat_num = int(data[idx])
  left_sum += dat_num

for idx in range(left_idx + 1, len(data)):
  dat_num = int(data[idx])
  right_sum += dat_num

if left_sum == right_sum:
  print("LUCKY")
else:
  print("READY")