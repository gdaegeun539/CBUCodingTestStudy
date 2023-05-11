from sys import stdin

input2 = stdin.readline


def fixed_parametric(arg_list, n):
  start = 0
  end = n - 1

  while start <= end:
    mid = (end + start) // 2
    if arg_list[mid] == mid:
      return mid
    elif arg_list[mid] > mid:
      end = mid - 1
    else:
      start = mid + 1

  return -1


n = int(input2().rstrip())
n_list = list(map(int, input2().rstrip().split()))

rslt = fixed_parametric(n_list, n)
print(rslt)