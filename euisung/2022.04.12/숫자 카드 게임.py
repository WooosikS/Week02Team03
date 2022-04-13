n, m = map(int, input().split())

res = 0
for i in range(n):
    arr = list(map(int, input().split()))
    min_value = 100000
    for j in arr:
        min_value = min(min_value, j)
    res = max(res, min_value)

print(res)
