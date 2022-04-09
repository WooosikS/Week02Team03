import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
n , c = map(int ,input().split())
house = [int(input()) for _ in range(n)]
house.sort()
start = 1
end = house[-1] - house[0]

result = 0
while start <= end:
  mid = (start+end)//2

  cnt = 1
  temp = house[0]

  for i in range(1, n):
    if house[i] >= temp+mid:
      cnt +=1
      temp = house[i]
  
  if cnt >=c:
    start = mid +1
    result = mid
  else:
    end = mid-1
print(mid)
print(result)