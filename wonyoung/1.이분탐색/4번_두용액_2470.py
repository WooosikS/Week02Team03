# 새로 풀어 보기
import sys
sys.stdin = open('input.txt', 'r')

n = int(input())
arr = sorted(list(map(int, input().split())))

left = 0
right = n-1
answer = arr[left] + arr[right]

a= arr[left]
b = arr[right]
while left < right:
  temp = arr[left] + arr[right]
  if abs(temp) < abs(answer):
    a = arr[left]
    b = arr[right]
    answer = temp
  
  if temp > 0 :
    right-=1
  else:
    left +=1

print(a,b)