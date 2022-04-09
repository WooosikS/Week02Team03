# c^n 은
# n이 짝수 일 때 c^n/2 * c^n/2
# n이 홀수 일 때 c^ n-1/2 * c^ n-1/2 * c
import sys
sys.setrecursionlimit(10**6)
sys.stdin = open('input.txt', 'r')

a,b,c = map(int, input().split())

def multi(a, b):
  if b == 1:
    return a

  else:
    x = multi(a, b//2)
    x %=c
    if b%2 == 0:
      return x*x
    else:
      return x*x*a

print(multi(a,b)%c)
