import sys
sys.stdin = open('input.txt', 'r')

n, k = map(int, input().split())
characters = [int(input()) for _ in range(n)]
characters.sort()

start = characters[0]
end = characters[0] + k
result = 0
while start <= end:
  mid = (start+end)//2
  
  total = 0
  # 임시 목표 mid값을 달성하는데 걸리는 총 레벨 찾기
  for charac in characters:
    if mid - charac >0:
      total += mid - charac
  
  if k < total:
    end = mid-1
  elif k >= total:
    result = mid
    start = mid +1

print(result)


