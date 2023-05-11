from sys import stdin

input2 = stdin.readline

n = int(input2().rstrip())

cords = []
for _ in range(n):
    x, y = map(int, input2().rstrip().split())
    cords.append((x, y))

cords.sort(key=lambda x: (x[0], x[1]))

for cord in cords:
    print(f"{cord[0]} {cord[1]}")
