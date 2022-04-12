# 이러면 당연히 시간초과 난다~~~

# import sys

# num = int(sys.stdin.readline())

# queue_list = []

# for i in range(1, num+1):
#     queue_list.append(i)


# for i in range(num-1):
#     del queue_list[0]
#     queue_list[-1], queue_list[0] = queue_list[0], queue_list[-1]

# print(queue_list)

import sys
from collections import deque

num = int(sys.stdin.readline())
q = deque([i for i in range(1, num+1)])

while len(q) > 1:
    q.popleft()
    movemove = q.popleft()
    q.append(movemove)

print(q[0])