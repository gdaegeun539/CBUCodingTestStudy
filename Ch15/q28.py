"""
12분 소요
"""
from sys import stdin


def find_point(n, elems):
  start, end = 0, n

  while start <= end:
    mid = (end + start) // 2

    if mid == elems[mid]:
      return mid
    elif mid < elems[mid]:
      end = mid - 1
      continue
    else:
      start = mid + 1
      continue

  return -1


n = int(input())
elems = list(map(int, stdin.readline().rstrip().split()))
rslt = find_point(n, elems)
print(rslt)
