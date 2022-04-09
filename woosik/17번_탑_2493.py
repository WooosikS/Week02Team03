# 내가 어떻게 하려고 하는거냐면 제일 오른쪽 기둥을 기준 잡는다.
# 스택배열 pop 해서 list[-1] == max 랑 비교해서 크면 걔의 배열 순서를 저장한다.
# 그리고 max를 다시 list[-1] 에서 다시 왼쪽으로 옮긴다.
# 그리고 왼쪽에서 자기보다 큰 애 찾아서 찾았으면 배열 순서를 저장한다.
# 그러면 시간초과 난다.


import sys

num = int(sys.stdin.readline())

llist = list(map(int, sys.stdin.readline().split()))
answer = [0 for _ in range(num)]

stack = []

for i in range(num):
    while stack:
        if stack[-1][1] > llist[i]:
            answer[i] = stack[-1][0] + 1
            break
        else:
            stack.pop()
    stack.append([i, llist[i]])
print(*answer)
