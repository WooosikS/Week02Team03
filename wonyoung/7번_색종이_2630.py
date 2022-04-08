import sys

sys.stdin = open('input.txt', 'r')

n = int(input())
paper = [list(map(int, input().split())) for _ in range(n)]
result = [0,0]

# 종이가 하나의 색으로 되어 있는지 확인
def check(n,x,y):
  temp = paper[x][y]
  for i in range(x,n+x):
    for j in range(y, n+y):
      if temp != paper[i][j]:
        return False
  return True


def cut_paper(n,x,y):
  if check(n,x,y):
    result[paper[x][y]] +=1
    return
  n //=2
  # 하나의 색이 아닌 종이는 4등분으로 자름
  cut_paper(n, x, y)
  cut_paper(n, x, y+n)
  cut_paper(n, x+n, y)
  cut_paper(n, x+n, y+n)

cut_paper(n,0,0)
print(result[0])
print(result[1])