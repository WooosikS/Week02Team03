# 이전 곱셈 문제와 매우 유사하다.
# 곱셈문제와 달리 숫자 계산이 아닌 행렬계산이라는 차이가 있다.
# 행렬을 쪼게서 계산하는 부분을 잘 만들어야함
# 다시 풀어보기
import sys

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

n, b = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]

def mod(mat):
  for i in range(n):
    for j in range(n):
      mat[i][j] = (mat[i][j])%1000
  return mat

def multi(A, B):
  n = len(A)
  temp = [[0]*n for _ in range(n)]
  for i in range(n):
    for j in range(n):
      for k in range(n):
        temp[i][j] += (A[i][k]*B[k][j])
  
  return temp

def sol(matrix, b):
  if b == 1:
    # 그냥 메트릭스 리턴
    return mod(matrix)
  else:
    temp = sol(matrix, b//2)

    if b % 2 == 0:
      return mod(multi(temp,temp))
    else:
      return mod(multi(multi(temp,temp), matrix))


for mat in (sol(matrix, b)):
  print(*mat)
