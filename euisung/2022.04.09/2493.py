import sys

n = int(sys.stdin.readline())
stack = list(map(int, sys.stdin.readline().split()))
cnt = 1
arr = []
point = stack[-1]

for i in range(n):
    for j in range(n):
        if point < stack[n-i-1]:
            cnt += 1
            point = stack[n-i-1]
    arr.append(stack.pop())

print(arr)
