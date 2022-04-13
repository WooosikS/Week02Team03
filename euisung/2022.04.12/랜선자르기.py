def Count(len):
    cnt = 0
    for x in arr:
        cnt += (x//len)
    return cnt


n, k = map(int, input().split())
arr = [int(input()) for _ in range(n)]
res = 0

start = 1
end = max(arr)

while start <= end:
    center = (start + end) // 2
    if Count(center) >= k:
        res = center
        start = center + 1
    else:
        end = center - 1
print(res)
