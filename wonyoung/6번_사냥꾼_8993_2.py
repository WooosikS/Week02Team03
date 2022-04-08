# 동물 찾는 것을 이분탐색해야할 거 같은데 
# 좌표를 어떻게 하나
import sys
sys.stdin = open('input.txt', 'r')

m, n, l = map(int ,input().split())
shooters = sorted(list(map(int, input().split())))
animals = []
for i in range(n):
  x, y = map(int, input().split())
  animals.append((x,y))

animals = sorted(animals, key= lambda x: x[0]**2+x[1]**2)