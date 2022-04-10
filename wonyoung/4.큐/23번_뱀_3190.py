from collections import deque
import sys

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

n = int(input())
board = [[0]*n for _ in range(n)]
k = int(input())
for _ in range(k):
  x, y = map(int, input().split())
  board[x-1][y-1] = 2

l = int(input())
command = deque()
for i in range(l):
  x, c = input().split()
  command.append((int(x),c))

board[0][0] = 1
snake = deque([[0,0]])

length = 1
# 상우하좌 이동
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
direct = 1
time = 0
while True:
  # 명령 실행
  if command and time == command[0][0]:
    if command[0][1] == 'D':
      direct -=1
      if direct <0:
        direct = 3
    else:
      direct +=1
      if direct > 3:
        direct = 0
    command.popleft()
  
  nx, ny = snake[-1][0]+dx[direct], snake[-1][1]+dy[direct]
  if 0<= nx <=n-1 and 0<= ny <=n-1 and board[nx][ny] != 1:
    if board[nx][ny] == 2:
      board[nx][ny] = 1
      snake.append([nx,ny])
      time +=1
    else:
      board[nx][ny] = 1
      snake.append([nx,ny])
      tx, ty = snake.popleft()
      board[tx][ty] = 0
      time +=1
  else:
    time +=1
    break

print(time)
