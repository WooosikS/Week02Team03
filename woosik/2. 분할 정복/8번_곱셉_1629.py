# 1. b의 값이 짝수인지 홀수인지 파악한다.
# 2. b의 값이 짝수라면 10 ^10 -> (10^5)^2 형태로 바꿔준다.
# 3. b의 값이 홀수라면 10 ^11 -> (10^5)^2 * 10 형태로 바꿔준다.

import sys
def solution(a, b):
    if b == 1:
        return a%c
    else:
        temp = solution(a, b//2)
        if b % 2 == 0:
            return temp * temp % c
        else:
            return temp * temp * a % c

a, b, c = map(int, sys.stdin.readline().split())
result = solution(a, b)
print(result)