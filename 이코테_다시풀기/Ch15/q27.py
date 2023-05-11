from sys import stdin
import bisect

input2 = stdin.readline

n, x = map(int, input2().rstrip().split())

elems = list(map(int, input2().rstrip().split()))

left_idx = bisect.bisect_left(elems, x)
right_idx = bisect.bisect_right(elems, x)

if left_idx == right_idx:
  print(-1)
else:
  print(right_idx - left_idx)
