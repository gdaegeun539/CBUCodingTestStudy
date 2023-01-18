first_list = list(input().split(" "))
N = int(first_list[0])
M = int(first_list[1])
K = int(first_list[2])
# N, M, K

input_arr = list(map(int, list(input().split(" "))))

input_arr = sorted(input_arr, reverse=True)

rslt = 0

if (input_arr[0] == input_arr[1]):
  rslt = input_arr[0] * M
else:
  times = 1
  for loop in range(0, M):
    if (times <= K):
      rslt += input_arr[0]
      times += 1
    else:
      rslt += input_arr[1]
      times = 1

print(rslt)
