# 답지 봄, 다시 풀기
import heapq
import sys

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

n = int(input())
temp_HO = [sorted(list(map(int, input().split()))) for _ in range(n)]
d = int(input())

ho =[]
for HO in temp_HO:
  if abs(HO[0]-HO[1])<=d:
      ho.append(HO)

ho = sorted(ho, key= lambda x:x[1])

heap = []
answer = 0
for home, office in ho:
  if not heap:
    heapq.heappush(heap, (home, office))
  else:
    while heap[0][0] < office - d:
      heapq.heappop(heap)
      if not heap:
        break
    heapq.heappush(heap, (home, office))
    answer = max(answer, len(heap))

print(answer)