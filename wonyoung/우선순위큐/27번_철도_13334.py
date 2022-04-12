# 답지 봄, 다시 풀기
# 우선순위큐 사용시점: 특정 시점에 최대값 or 최솟값을 필요로 할때
# 스택 사용시점: 특정 시점에 지금까지 받은 데이터들의 마지막 원소를 참조하나? 란 생각을 염두할때
# import heapq
# import sys

# sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline

# n = int(input())
# temp_HO = [sorted(list(map(int, input().split()))) for _ in range(n)]
# d = int(input())

# ho =[]
# for HO in temp_HO:
#   if abs(HO[0]-HO[1])<=d:
#       ho.append(HO)

# ho = sorted(ho, key= lambda x:x[1])

# heap = []
# answer = 0
# for home, office in ho:
#   if not heap:
#     heapq.heappush(heap, (home, office))
#   else:
#     while heap[0][0] < office - d:
#       heapq.heappop(heap)
#       if not heap:
#         break
#     heapq.heappush(heap, (home, office))
#     answer = max(answer, len(heap))

# print(answer)


import sys, heapq
input = sys.stdin.readline
n = int(input())
commuting = []
for _ in range(n):
    home, office = map(int, input().split())
    commuting.append([min(home, office), max(home, office)])
d = int(input())

# 끝 점 기준 sorting
commuting.sort(key=lambda x:x[1]) 

cnt = 0
max_cnt = 0
h = []
for i in range(n):
    end = commuting[i][1]
    if commuting[i][1] - commuting[i][0] <= d:
        heapq.heappush(h, commuting[i])
    while len(h)>0:
        if end-h[0][0] > d: # 끝 점이 갱신됐을 때 맨 앞 home이 d안에 포함되지 않는다면
            heapq.heappop(h)
        else: # 포함된다면 확인 끝
            break
    max_cnt = max(len(h), max_cnt)

print(max_cnt)