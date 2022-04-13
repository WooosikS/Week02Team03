import heapq
n = int(input())
card = [int(input()) for _ in range(n)]
card.sort()
result = 0
for i in range(0, n):
    if len(card) == 1:
        print(0)
    while len(card) > 1:
        temp_1 = heapq.heappop(card)
        temp_2 = heapq.heappop(card)
        result += temp_1 + temp_2
        heapq.heappush(card, temp_1 + temp_2)
print(result)
