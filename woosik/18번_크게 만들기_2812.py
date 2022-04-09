# N 자리 숫자 K 개 지워서
# list에서 맨 뒤, 맨 뒤 -1 숫자 지우고 아닌거 최댓값 아니면 맨뒤, 맨 뒤 -2
# 또 아니면 맨 뒤, 맨 뒤-3 하나씩 비교해서 최댓값 저장한 값 print()         하면 당연히 시간초과 나겠지?

import sys

x, y = map(int, sys.stdin.readline().split())

num = int(sys.stdin.readline())

