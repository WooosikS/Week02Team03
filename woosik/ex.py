import sys
from collections import deque

num = int(sys.stdin.readline())

apple = [[0] * num for _ in range(num)]

print(*apple)