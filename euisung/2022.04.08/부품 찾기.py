def search(start, end, key, arr):
    while start <= end:
        center = (start + end)//2
        if arr[center] == key:
            return center
        elif arr[center] > key:
            end = center - 1
        elif arr[center] < key:
            start = center + 1
    return None

# def search(start, end, arr):
#     center = (start + end)//2
#     print(arr[center])


N = int(input())
N_arr = list(map(int, input().split()))
N_arr.sort()
M = int(input())
M_arr = map(int, input().split())

for i in M_arr:
    print(search(0, N-1, i, N_arr))
