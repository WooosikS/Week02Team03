T = int(input())


def sol(i):
    if i == 1:
        return 1
    elif i == 2:
        return 2
    elif i == 3:
        return 4
    else:
        return sol(i-1)+sol(i-2)+sol(i-3)


for i in range(T):
    n = int(input())
    print(sol(n))
