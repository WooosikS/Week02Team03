from collections import deque

n, k = 7, 3
kill_list = deque(list(i for i in range(1,n+1)))

cnt = 1
answer = []
while kill_list:
  if cnt != k:
    kill_list.append(kill_list.popleft())
    cnt+=1
  else:
    answer.append(kill_list.popleft())
    cnt=1

s = '<'
for i in range(len(answer)):
  if i == n-1:
    s+= str(answer[i])+'>'
    break
  s+= str(answer[i])+', '

print(s)