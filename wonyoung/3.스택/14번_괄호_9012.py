import sys
sys.stdin = open('input.txt', 'r')

n = int(input())
for _ in range(n):
  vps = input()
  stack = []
  for i in vps:
    if len(stack) == 0 :
      stack.append(i)
    else:
      if stack[-1]=='(' and i ==')':
        stack.pop()
      else:
        stack.append(i)
  print('YES') if len(stack) == 0 else print('NO')

