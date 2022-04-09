import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

n = int(input())
stics = [int(input()) for _ in range(n)]

temp = stics[-1]
cnt = 1
for i in range(n):
  pop_stic = stics.pop()
  if pop_stic > temp:
    cnt +=1
    temp = pop_stic

print(cnt)