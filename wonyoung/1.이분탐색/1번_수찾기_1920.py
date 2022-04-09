import sys
sys.stdin = open('input.txt', 'r')

n = int(input())
n_list = list(map(int ,input().split()))
m = int(input())
m_list = list(map(int, input().split()))
n_list.sort()

def b_search(n):
  left = 0
  right = len(n_list)-1
  while left <= right:
    center = (left+right)//2
    if n_list[center] == n:
      return 1
    elif n_list[center] > n:
      right = center -1
    else:
      left = center+1
  return 0


for i in m_list:
  print(b_search(i))