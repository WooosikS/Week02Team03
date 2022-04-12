# 2^10은 2^5 * 2^5으로 나타낼 수 있다 (짝수)
# 2^11은 2^5 * 2^5 * 2로 나타낼 수 있다 (홀수)


a, b, c = map(int, input().split(' '))


def dnc(length):
    if length == 1:
        return a % c
    if length % 2 == 0:
        left = dnc(length // 2)
        return left * left % c
    else:
        left = dnc(length // 2)
        return left * left * a % c


print(dnc(b))
