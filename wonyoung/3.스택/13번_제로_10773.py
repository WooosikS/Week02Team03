import sys
sys.stdin = open('input.txt', 'r')

n = int(input())
stack = []
for _ in range(n):
  num = int(input())
  stack.pop() if num == 0 else stack.append(num)

print(sum(stack))