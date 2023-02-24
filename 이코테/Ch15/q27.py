"""
제한시간 30분 채움
답안이랑 다름
"""
import sys

idx = -1


def 기본이진탐색(find_val, start, end):
  global idx
  global elems
  if start > end:
    # cnt = -1
    return

  mid = (end + start) // 2

  if elems[mid] == find_val:
    if elems[mid - 1] == find_val and mid > 0:
      idx = mid - 1
      end = mid - 2
      기본이진탐색(find_val, start, end)
    else:
      idx = mid
      return

  elif elems[mid] > find_val:
    end = mid - 1
    기본이진탐색(find_val, start, end)
  else:
    start = mid + 1
    기본이진탐색(find_val, start, end)


n, x = map(int, input().split())
elems = list(map(int, sys.stdin.readline().rstrip().split()))

기본이진탐색(x, 0, n - 1)
cnt = 0
if idx != -1:
  for loop_idx in range(idx, n):
    # print(f"cnt: {cnt}, idx: {idx}")
    if elems[loop_idx] != x:
      break
    cnt += 1
else:
  cnt = -1

print(cnt)
