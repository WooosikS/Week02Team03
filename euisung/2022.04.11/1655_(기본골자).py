import heapq

n = int(input())
heap = []
arr_low = []
arr_high = []

for _ in range(1, n+1):
    heapq.heappush(heap, int(input()))

    if len(heap) % 2 == 0:
        if len(heap) == 1:
            print(heap[0])
        elif len(heap) == 2:
            if heap[0] < heap[1]:
                print(heap[0])
            else:
                print(heap[1])
        elif len(heap) == 3:
            print(heap[1])
        else:
            point = len(heap)//2
            if heap[point] < heap[point+1]:
                print(heap[point])
            else:
                print(heap[point+1])
    else:
        # if len(heap) == 1:
        #     print(heap[0])
        # elif len(heap) == 2:
        #     if heap[0] < heap[1]:
        #         print(heap[0])
        #     else:
        #         print(heap[1])
        if len(heap) == 3:
            print(heap[1])
        else:
            point = len(heap)//2
            print(heap[point])
