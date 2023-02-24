n, k = map(int, input().split())
# rslt_times = 0

# while n % k != 0:
#   n -= 1
#   rslt_times += 1
rslt_times = 0

while n > 1:
  reminder = n % k
  if reminder:
    rslt_times += reminder
    n -= reminder
    if n < 1:
      rslt_times = rslt_times - (1 - n)
  else:
    n = n // k
    rslt_times += 1
  print(f"n: {n}")

print(rslt_times)
