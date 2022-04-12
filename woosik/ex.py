import sys

K, N = map(int, sys.stdin.readline().split())

lan = [int(sys.stdin.readline().strip()) for _ in range(K)]

min_lan = 1
max_lan = max(lan)

while (min_lan<=max_lan):
    cnt = 0
    mid = (min_lan+max_lan)//2

    for i in lan:
        cnt = cnt + i//mid
    if cnt>=N:
            min_lan = mid + 1
    else:
            max_lan = mid -1
print(max_lan)