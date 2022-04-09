n, m = map(int, input().split())
rice = list(map(int, input().split()))
start = 0
end = max(rice)
result = 0

while start <= end:
    cutline = (start + end)//2
    total = 0
    for i in rice:
        if i > cutline:
            total += i - cutline
    if total < m:
        end = cutline - 1
    else:
        result = cutline
        start = cutline + 1

print(result)
