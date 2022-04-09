import sys

N, M = map(int, sys.stdin.readline().split())
heights = list(map(int, sys.stdin.readline().strip().split()))


def cutTree(H):
    global heights
    ans = 0
    for i in heights:
        if i - H > 0:
            ans += i - H
    return ans


def binary_search(left, right):
    # print(left, right, end=' ')

    global N, M
    H = (left+right)//2

    if left > right:
        return H

    temp = cutTree(H)
    # print(f'cutTree({H}): {temp}')
    if temp == M:
        return H
    elif temp < M:
        return binary_search(left, H - 1)
    else:
        return binary_search(H + 1, right)


print(binary_search(0, max(heights)))
