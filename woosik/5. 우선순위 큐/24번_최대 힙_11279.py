import sys
import heapq

heap = []
num = int(sys.stdin.readline())

for _ in range(num):

    n = int(sys.stdin.readline())
    if n == 0 :
        if not heap == 0:
            print(0)
        else:
            print((-1)*heapq.heappop(heap))
    else:
        heapq.heappush(heap, (-1)*n)
