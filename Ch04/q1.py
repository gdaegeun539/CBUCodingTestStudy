# enum_x = (1,2,3,4,5,6,7,8)
len_x = 8
enum_y = ("a", "b", "c", "d", "e", "f", "g", "h")
len_y = 8

rslt = 0

temp = input()
# x_idx = enum_x.index(int(temp[0]))
y_idx = enum_y.index(temp[0]) + 1
x_idx = int(temp[1])

# 좌측 열 이동
if y_idx - 2 > 0:
  if x_idx - 1 > 0:
    rslt += 1
  if x_idx + 1 <= len_x:
    rslt += 1

# 우측 열 이동
if y_idx + 2 <= len_y:
  if x_idx - 1 > 0:
    rslt += 1
  if x_idx + 1 <= len_x:
    rslt += 1

# 상단 행 이동
if x_idx - 2 > 0:
  if y_idx - 1 > 0:
    rslt += 1
  if y_idx + 1 <= len_y:
    rslt += 1

# 하단 행 이동
if x_idx + 2 <= len_x:
  if y_idx - 1 > 0:
    rslt += 1
  if y_idx + 1 <= len_y:
    rslt += 1

print(rslt)