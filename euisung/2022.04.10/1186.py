import sys
from collections import deque

n, k = map(int, sys.stdin.readline().split())
que = deque()
dead_order = []

for i in range(1, n+1):
    que.append(i)

while que:
    for i in range(k-1):
        que.append(que.popleft())
    dead_order.append(que.popleft())

print("<", end='')
for i in range(len(dead_order)-1):
    print("%d, " % dead_order[i], end='')
print(dead_order[-1], end='')
print(">")
