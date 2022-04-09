def level_up(arr, center):
    t = 0
    for i in arr:
        if i >= center:
            break
        t += center - i
    return t


n, m = map(int, input().split())
level = sorted([int(input()) for _ in range(n)])
start = 0
end = max(level)
cnt = 0

while start <= end:
    center = (start + end) // 2
    if level_up(level, center) <= m:
        cnt = center
        start = center + 1
    else:
        end = center - 1
print(cnt)
