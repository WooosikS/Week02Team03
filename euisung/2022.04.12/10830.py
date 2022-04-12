
def mul(n, matrix, matrix2):
    result = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            for k in range(n):
                result[i][j] += matrix[i][k] * matrix2[k][j]
            result[i][j] %= 1000

    return result 


def devide(n, b, matrix):
    if b == 1:
        return matrix
    elif b == 2:
        return mul(n, matrix, matrix)
    else:
        tmp = devide(n, b//2, matrix)
        if b % 2 == 0:
            return mul(n, tmp, tmp)
        else:
            return mul(n, mul(n, tmp, tmp), matrix)


n, b = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

result = devide(n, b, arr)
for row in result:
    for num in row:
        print(num % 1000, end=' ')
    print()
