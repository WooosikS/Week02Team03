import sys

n = int(sys.stdin.readline())
n_list = list(map(int, sys.stdin.readline().split()))
n_list.sort()

m = int(sys.stdin.readline())
m_list = list(map(int, sys.stdin.readline().split()))

def binary_func(target):
    left = 0
    right = n - 1

    while left<=right:
        mid = ( left + right ) // 2
        if n_list[mid] == target:
            return True

        if n_list[mid] > target:
            right = mid - 1
        elif n_list[mid] < target:
            left = mid + 1

for i in range(m):
    if binary_func(m_list[i]):
        print(1)
    else:
        print(0)