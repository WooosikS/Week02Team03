import sys
import collections

n = int(sys.stdin.readline())
stack = collections.deque([])
result = 0

for _ in range(n):
    commend = int(input())
    if commend != 0:
        stack.append(commend)
    else:
        stack.pop()

for i in stack:
    result += i

print(result)
