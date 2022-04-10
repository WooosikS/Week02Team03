import sys
from collections import deque

N = int(sys.stdin.readline())

q_list = []
for i in range(N+1):
    q_list.append([0])
    for j in range(N+1):
        q_list[i].append([0])


