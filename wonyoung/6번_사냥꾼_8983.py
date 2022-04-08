# 60점까지 성공
import sys
sys.stdin = open('input.txt', 'r')

m, n, l = map(int ,input().split())
shooters = sorted(list(map(int, input().split())))
animals = []
for i in range(n):
  x, y = map(int, input().split())
  animals.append((x,y))
count_animal = len(animals)
animals = sorted(animals, key= lambda x: x[0]**2+x[1]**2)

for shooter in shooters:
  temp = []
  for animal in animals:
    if abs(shooter-animal[0]) + animal[1] <= l:
      temp.append(animal)
  animals = list(set(animals) - set(temp))

print(count_animal - len(animals))