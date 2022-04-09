import sys
input = sys.stdin.readline

n, m = map(int, input().split())
tree = list(map(int, input().split()))
start, end = 1, max(tree)

while start <= end:
    height = (start + end) // 2
    result = 0
    for i in tree:
        if i > height:
            result += i - height
    if result >= m:
        start = height + 1
    else:
        end = height - 1

print(end)
