n, m = map(int, input().split())

arr = list(map(int, input().split()))
arr.sort()
start = 1
end = len(arr)

# print(arr.index(m+1))

while start <= end:
    center = (start + end) // 2

    if arr[center] == m:
        print(center + 1)
        break
    elif arr[center] < m:
        start = center + 1
    else:
        end = center - 1
