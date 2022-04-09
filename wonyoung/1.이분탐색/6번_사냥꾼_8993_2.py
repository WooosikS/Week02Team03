# 동물의 x좌표 기준으로 사냥꾼의 위치를 이분탐색 한다.
# 
import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

m, n, l = map(int ,input().split())
shooters = sorted(list(map(int, input().split())))
animals = [list(map(int ,input().split())) for _ in range(n)]

cnt = 0
for a, b in animals:
  start = 0
  end = len(shooters)-1
  while start < end:
    mid = (start+end)//2

    if shooters[mid] < a:
      start = mid+1
    else:
      end = mid

  if abs(shooters[end]-a) + b <=l or abs(shooters[end-1]-a) + b <=l:
    cnt+=1
print(cnt)