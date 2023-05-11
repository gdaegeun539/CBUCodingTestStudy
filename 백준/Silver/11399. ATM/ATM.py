from sys import stdin

input2 = stdin.readline

n = int(input2().rstrip())

times = list(map(int, input2().rstrip().split()))

times.sort()

rslt = times[0]
acc_times = times[0]
for idx in range(1, n):
    acc_times += times[idx]
    rslt += acc_times

print(rslt)
