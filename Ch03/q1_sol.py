N, M, K = map(int, input().split())

dat = list(map(int, input().split()))

dat = sorted(dat, reverse=True)

quot = M // (K + 1)
reminder = M % (K + 1)
arr_sum = dat[0] * K + dat[1]

rslt = arr_sum * quot + dat[0] * reminder

print(rslt)
