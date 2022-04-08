# 오후에 다시 풀어보기
import sys
sys.stdin = open('input.txt', 'r')

n , c = map(int ,input().split())
arr = [int(input()) for _ in range(n)]
arr.sort()
print(arr)