n = int(input())
n_arr = list(map(int, input().split()))
m = int(input())
m_arr = list(map(int, input().split()))

result_arr = n_arr + m_arr
result_arr.sort()

for i in result_arr:
    print(i, end=' ')
