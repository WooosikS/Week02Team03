import sys

num = int(sys.stdin.readline())

stack = []
count = 1

for _ in range(num):
    stack.append(int(sys.stdin.readline()))

max = stack[-1]

for i in reversed(range(num)):
    if stack[i] > max:
        count += 1
        max = stack[i]

print(count)