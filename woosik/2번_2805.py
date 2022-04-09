import sys

N, M = map(int, sys.stdin.readline().split())
trees = list(map(int, sys.stdin.readline().split()))

def cutting(cutter):
    length = 0
    for tree in trees:
        rest = tree - cutter
        if rest > 0:
            length += rest
    return length

def findCutter(start, end, aim):
    if start > end:
        return end
    
    mid = (start + end) // 2
    if cutting(mid) >= aim:
        return findCutter(mid+1, end, aim)
    else:
        return findCutter(start, mid-1, aim)

print(findCutter(1, max(trees), M))