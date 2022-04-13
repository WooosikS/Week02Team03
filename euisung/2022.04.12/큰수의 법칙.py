n, k, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
result = 0

for i in range(k):

    cnt = 0

    if cnt != 3:
        result += max(arr)
        cnt += 1
    else:
        result += arr[-2]
        cnt = 0

print(result)
