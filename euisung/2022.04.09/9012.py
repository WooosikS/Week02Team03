import sys
import collections

n = int(sys.stdin.readline())
stack = collections.deque([list(input()) for _ in range(n)])

for i in stack:
    cnt = 0
    for j in i:
        if j == "(":
            cnt += 1
        elif j == ")":
            cnt -= 1

        if cnt < 0:
            break

    if cnt == 0:
        print("YES")
    else:
        print("NO")
