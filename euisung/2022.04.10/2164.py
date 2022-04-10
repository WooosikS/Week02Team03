import sys
from collections import deque

n = int(sys.stdin.readline())
cnt = 1
que = deque()
for i in range(1, n+1):
    que.append(i)

while len(que) > 1:
    if cnt % 2 != 0:
        que.popleft()
        cnt += 1
    else:
        que.rotate(-1)
        cnt += 1

print(que[0])
