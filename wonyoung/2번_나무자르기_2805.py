# 파이썬은 시간 초과가 발생하여 pypy로 제출 후 정답
import sys
sys.stdin = open('input.txt', 'r')

n, m = map(int, input().split())
woods = sorted(list(map(int, input().split())))

left = 0
right= woods[-1]
result = -1e9
while left<=right:
  center = (left+right)//2
  temp = 0
  for wood in woods:
    if wood-center > 0:
      temp += wood-center
  if temp>=m:
    # 자른 길이가 m과 같거나 클때
    result = max(result, center)
    left = center+1
  else:
    # 자른 길이가 m보다 작다면
    right = center-1

print(result)
