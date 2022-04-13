def Count(capacit):
    cnt = 1
    hap = 0
    for x in arr:
        if hap+x > capacit:
            cnt += 1
            hap = x
        else:
            hap += x
    return cnt


n, k = map(int, input().split())
arr = list(map(int, input().split()))

start = 1
end = sum(arr)
res = 0

while start <= end:
    center = (start + end) // 2
    if Count(center) <= k:
        res = center
        end = center - 1
    else:
        start = center + 1

print(res)
