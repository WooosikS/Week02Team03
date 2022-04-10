import sys
from collections import deque

n = int(sys.stdin.readline())
que = deque()

for _ in range(n):
    que_commend = sys.stdin.readline().split()

    if que_commend[0] == "push":
        que.append(que_commend[-1])
    elif que_commend[0] == 'pop':
        if not que:
            print(-1)
        else:
            print(que.popleft())
    elif que_commend[0] == 'size':
        print(len(que))
    elif que_commend[0] == 'empty':
        if not que:
            print(1)
        else:
            print(0)
    elif que_commend[0] == 'front':
        if not que:
            print(-1)
        else:
            print(que[0])
    elif que_commend[0] == 'back':
        if not que:
            print(-1)
        else:
            print(que[-1])
