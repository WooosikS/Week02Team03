word = input()
res = 0
cnt = 0
for i in word:
    # isdigit = 숫자 형태 [ex) 2^2, 2^3] 면 모두 파악해줌
    # isDecimal = 0~9 형태의 숫자만 파악해줌
    if i.isdecimal():
        res = res*10 + int(i)
print(res)

for x in range(1, res+1):
    if res % x == 0:
        cnt += 1
print(cnt)
