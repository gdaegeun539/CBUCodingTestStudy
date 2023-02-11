import sys


def 높이찾기(start, end, n, elem_n, m):
  get_list = [0] * n
  temp_total = 0

  mid = 0
  while start <= end:
    mid = (end + start) // 2
    print(f"mid: {mid}")

    for idx in range(n):
      temp_len = elem_n[idx] - mid
      get_list[idx] = temp_len if temp_len >= 0 else 0
    print(f"get_list: {get_list}")

    temp_total = sum(get_list)
    print(f"temp_total: {temp_total}")
    if temp_total == m:
      return mid
    elif temp_total < m:
      end = mid - 1
    else:
      start = mid + 1

  if temp_total < m:
    return mid - 1
  else:
    return mid


n, m = map(int, sys.stdin.readline().rstrip().split())
elem_n = list(map(int, sys.stdin.readline().rstrip().split()))

end = max(elem_n)
h = 높이찾기(0, end, n, elem_n, m)

print(f"\n{h}")
