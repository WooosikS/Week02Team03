n = int(input())
score = map(int, input().split())
result = 0
hap = 0

for i in score:
    if i == 1:
        result += 1
        hap += (result * 1)
    elif i == 0:
        result = 0

print(hap)
