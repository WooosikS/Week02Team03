n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
result = 0

for i in range(n):
    hap_1 = 0
    hap_2 = 0
    for j in range(n):
        hap_1 += arr[i][j]
        hap_2 += arr[j][i]
    if hap_1 > result:
        result = hap_1
    if hap_2 > result:
        result = hap_2

hap_1 = 0
hap_2 = 0

for i in range(n):
    hap_1 += arr[i][i]
    hap_2 += arr[i][n-i-1]

if hap_1 > result:
    result = hap_1
if hap_2 > result:
    result = hap_2

print(result)
