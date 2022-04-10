import heapq
import sys

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

n = int(input())
card = []
for _ in range(n):
  heapq.heappush(card, int(input()))

answer = []
while len(card) != 1:
  a = heapq.heappop(card)
  b = heapq.heappop(card)
  answer.append(a+b)
  heapq.heappush(card, a+b)

print(sum(answer))

