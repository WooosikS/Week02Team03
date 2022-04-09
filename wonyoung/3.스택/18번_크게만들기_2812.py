import sys
sys.stdin = open('input.txt', 'r')

def sol():
  n, k = map(int, input().split())
  numbers = list(map(int,str(input())))

  stack = []
  
  for idx ,num in enumerate(numbers):
    if len(stack) == 0:
      stack.append(num)
      continue
    
    if stack[-1] >= num:
      stack.append(num)
    else:
      while len(stack) > 0 and stack[-1] <num and k !=0:
        stack.pop()
        k-=1
      stack.append(num)
    
    if k == 0:
      temp = numbers[idx+1:]
      for i in temp:
        stack.append(int(i))
      break
  if k>0:
    for _ in range(k):
      stack.pop()
  print(''.join(list(map(str, stack))))

sol()