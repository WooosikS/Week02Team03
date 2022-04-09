import sys

num = int(sys.stdin.readline())

for _ in range(num):
    llist = list(sys.stdin.readline())
    sum = 0
    for i in llist:
        if i == '(':
            sum += 1
        elif i == ')':
            sum -= 1
        if sum < 0:
            print("NO")
            break
    if sum > 0:
        print('NO')
    elif sum == 0:
        print("YES")