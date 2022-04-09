import sys

n, k = map(int, sys.stdin.readline().split())
number = list(sys.stdin.readline().strip())
arr = []
cnt = 0

for i in range(n):
    while cnt != k and arr and arr[-1] < number[i]:  # 리스트가 비어있으면 False
        arr.pop()
        cnt += 1
    arr.append(number[i])

print("".join(arr[:n-k]))
