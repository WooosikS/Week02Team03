# 최소 힙으로 풀 생각을 먼저 했다.
#  card 숫자 받고 heapify 써서 정렬 후 두 카드 꺼내서 더하고 다시 넣고, 합한 카드랑 뒷 카드랑 더한다.

import heapq
import sys

num = int(sys.stdin.readline())
heap = []
cnt = 0

for _ in range(num):
    card = int(sys.stdin.readline())
    heapq.heappush(heap, card)

heapq.heapify(heap)

if len(heap) == 1 :
    print(0)
else:
    # while len(heap) > 1:      둘 다 가능
    for _ in range(num-1):
        temp1 = heapq.heappop(heap)
        temp2 = heapq.heappop(heap)
        cnt += temp1 + temp2
        heapq.heappush(heap, temp1+temp2)
    print(cnt)
