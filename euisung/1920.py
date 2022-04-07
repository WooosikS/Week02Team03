n = int(input())
arr_n = sorted(map(int, input().split()))
m = int(input())
arr_m = map(int, input().split())


def search(arr, key, start, end):
    # arr = 찾을려고 하는 키 값이 있는 배열, Key = 찾을려고 하는 값
    # start = 검색 범위의 맨 앞, end = 검색 범위의 맨 뒤. 이진검색을 위해 범위를 정함

    if start > end:
        return 0

    pc = (start+end) // 2  # 인덱스의 정중앙
    if arr[pc] == key:
        return 1
    elif arr[pc] < key:
        return search(arr, key, pc+1, end)
    else:
        return search(arr, key, start, pc-1)


for i in arr_m:
    print(search(arr_n, i, 0, len(arr_n)))
