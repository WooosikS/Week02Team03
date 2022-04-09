# print 문의 속도가 느려서 바로 출력하지 않고
# answer 배열에 담아서 출력하도록 풀이
import sys
sys.stdin = open('input.txt', 'r')

def sol():
  n = int(input())
  stack = []
  answer = []
  for _ in range(n):
    command = list(input().split())
    if command[0] == 'push':
      stack.append(command[1])
    elif command[0] == 'pop':
      answer.append(stack.pop()) if len(stack) !=0 else answer.append(-1)
    elif command[0] == 'size':
      answer.append(len(stack))
    elif command[0] == 'empty':
      answer.append(0) if len(stack) !=0 else answer.append(1)
    else:
      answer.append(stack[-1]) if len(stack) !=0 else answer.append(-1)
  
  for i in answer:
    print(i)

sol()