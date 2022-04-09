import sys

n, k = map(int, sys.stdin.readline().split())
number = sys.stdin.readline()
arr = [number[0]]
cnt = 0

for i in range(1, n):
    if cnt == k:
        break

    if arr[-1] < number[i]:
        cnt += 1
        arr.pop()

    arr.append(number[i])

print(arr)
