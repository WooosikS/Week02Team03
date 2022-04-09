import sys

n, k = map(int, sys.stdin.readline().split())
number = list(map(int, sys.stdin.readline().strip()))
point = number[0]
stack = []
cnt = 0

for i in range(1, len(number)+1):
    if cnt == k:
        break

    if number[i] < point:
        number.pop(i)
    elif number[i] > point:
        cnt += 1
        number.remove(point)
        point = number[i]

print(number)
