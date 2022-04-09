import sys

n = int(sys.stdin.readline())
stack = [int(sys.stdin.readline()) for _ in range(n)]
cnt = 1
point = stack[-1]

for i in range(n):
    if point < stack[n-i-1]:
        cnt += 1
        point = stack[n-i-1]

print(stack.pop())
