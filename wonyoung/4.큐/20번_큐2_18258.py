from collections import deque
import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

n = int(input())
q = deque()
answer = []
for _ in range(n):
  command = list(input().split())
  
  if command[0] == 'push':
    q.append(int(command[1]))
  elif command[0] == 'pop':
    if q: answer.append(q.popleft())
    else: answer.append(-1)     
  elif command[0] == 'size':
    answer.append(len(q))
  elif command[0] == 'empty':
    if q:answer.append(0)
    else: answer.append(1)
      
  elif command[0] == 'front':
    if q:answer.append(q[0])
    else: answer.append(-1)
  else:
    if q:answer.append(q[len(q)-1])
    else: answer.append(-1)

for i in answer:
  print(i)