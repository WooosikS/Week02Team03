import sys

num = int(sys.stdin.readline())

stk = []

for _ in range(num):
    num = int(sys.stdin.readline())
    if num == 0:
        stk.pop()
    else:
        stk.append(num)
print(sum(stk))