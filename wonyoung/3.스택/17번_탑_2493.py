import sys
sys.stdin = open('input.txt', 'r')

n = int(input())
tops = list(map(int, input().split()))
answer = [0]*n

stack = []

for i in range(len(tops)):
  if len(stack) == 0:
    stack.append((i,tops[i]))
  else:
    if tops[i] > stack[-1][1]:
      while len(stack) != 0 and tops[i] > stack[-1][1]:
        stack.pop()
      
      if len(stack) != 0:
        answer[i] = stack[-1][0]+1
      stack.append((i,tops[i]))
      
    else:
      answer[i] = stack[-1][0]+1
      stack.append((i,tops[i]))

print(answer)