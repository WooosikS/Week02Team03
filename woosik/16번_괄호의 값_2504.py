import sys

llist = sys.stdin.readline().strip()

stack = []
tmp = 1
res = 0

for i in range(len(llist)):
  if llist[i] == '(':
    tmp *= 2
    stack.append(llist[i])
  elif llist[i] == '[':
    tmp *= 3
    stack.append(llist[i])

    # 닫은 괄호일 때 스택의 TOP에 있는 것이 '[' 이거나 비어있다면 break

# 여는 괄호를 스택에 넣을 때, 그냥 push만 할 것이 아니라 해당 괄호에 해당하는 값을 temp에 곱한다. 
# 이 때, 이 temp의 초기값은 1이어야 한다. 0으로 하면 곱해봤자 0이므로 꼭 1로 초기화해야 한다.

# 닫는 괄호가 나올 때, 
# 지금 검사하는 것의 이전 인덱스의 괄호가 짝이 맞아서 쌍을 이루는 괄호라면 
# temp를 최종 결과인 res에 더한다. 그 후 temp를 해당 괄호에 해당하는 값으로 나눈 뒤, 괄호를 계산한 셈이므로 pop하면 된다.
# 최종적으로는 res가 답이 된다. 



  elif llist[i] == ')':
    if not stack or stack[-1] == '[':
      res = 0
      break
    if llist[i-1] == '(':
      res += tmp
    tmp //= 2
    stack.pop() 
  
  else:
    if not stack or stack[-1] == '(':
      res = 0
      break
    # [()]의 경우 ] 직전 문자가 )이므로 더하지 않고 넘어감
    # 단, 이 경우는 오류는 아님
    if llist[i-1] == '[':
      res += tmp
    tmp //= 3
    stack.pop() # pop 까먹지 말기

if stack:
  res = 0
print(res)