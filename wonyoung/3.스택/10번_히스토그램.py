from collections import deque
import sys
sys.stdin = open('input.txt', 'r')
while True:
    rec = list(map(int, sys.stdin.readline().split()))
    n = rec.pop(0)

    if n == 0:
        break

    stack = deque()
    answer = 0

    # 왼쪽부터 차례대로 탐색
    for i in range(n):
        while len(stack) != 0 and rec[stack[-1]] > rec[i]:
            tmp = stack.pop()

            if len(stack) == 0:
                width = i
            else:
                width = i - stack[-1] - 1
            answer = max(answer, width * rec[tmp])
        stack.append(i)

    # 스택에 남아있는 것을 처리
    while len(stack) != 0:
        tmp = stack.pop()

        if len(stack) == 0:
            width = n
        else:
            width = n - stack[-1] - 1
        answer = max(answer, width * rec[tmp])

    print(answer)

# import sys
# sys.stdin = open('input.txt', 'r')

# while True:

#   input_list= list(map(int, input().split()))
#   n = input_list.pop(0)
#   if n == 0:
#     break
#   input_list.append(0)
#   stack = []

#   answer = 0
#   for i in range(n+1):
#     if not stack:
#       stack.append((i, input_list[i]))
#     else:
#       if stack[-1][1] <= input_list[i]:
#         stack.append((i, input_list[i]))
#       else:
#         cnt = 0
#         index = 0
#         while stack and stack[-1][1] >= input_list[i]:        
#           cnt += 1
#           index, h = stack.pop()
#           temp = cnt*h
#           answer = max(answer, temp)
#         stack.append((index,input_list[i]))
#   print(answer)
