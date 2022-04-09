n, c = map(int, input().split())
arr = []

for i in range(n):
    arr.append(int(input()))

arr.sort()


def search(array, start, end):
    global result
    while start <= end:
        center = (start + end) // 2
        point = arr[0]
        cnt = 1

        for i in range(1, len(array)):
            if array[i] >= point+center:
                cnt += 1
                point = array[i]

        if cnt >= c:
            start = center + 1
            result = center
        else:
            end = center - 1


start = 1
end = max(arr) - min(arr)
result = 0

print(search(arr, start, end))
