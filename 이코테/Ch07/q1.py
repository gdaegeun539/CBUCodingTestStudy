import sys


def 부품찾기(n, n_dat, 찾을거):
  start = 0
  end = n
  mid = n // 2
  rslt = "no"

  for _ in range(n // 2 + 1):
    if start > end:
      break
    elif 찾을거 == n_dat[mid]:
      rslt = "yes"
      break
    elif 찾을거 > n_dat[mid]:
      start = mid
      mid += 1
    else:  # 찾을거 < n_dat[mid]
      end = mid
      mid -= 1

  return rslt


n = int(input())
n_dat = list(map(int, sys.stdin.readline().rstrip().split()))
n_dat.sort()

m = int(input())
m_dat = list(map(int, sys.stdin.readline().rstrip().split()))
is_m_in = [0] * m

for idx, data in enumerate(m_dat):
  is_m_in[idx] = 부품찾기(n, n_dat, data)

for elem in is_m_in:
  print(elem, end=" ")
print()
