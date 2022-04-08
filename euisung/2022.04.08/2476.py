n = int(input())
dice = [list(map(int, input().split())) for _ in range(n)]
max_gold = 0

for i in range(n):
    result = 0
    if dice[i][0] == dice[i][1] and dice[i][0] == dice[i][2] and dice[i][1] == dice[i][2]:
        result = 10000 + (dice[i][0] * 1000)
    elif dice[i][0] == dice[i][1]:
        result = 1000 + (dice[i][0] * 100)
    elif dice[i][0] == dice[i][2]:
        result = 1000 + (dice[i][0] * 100)
    elif dice[i][1] == dice[i][2]:
        result = 1000 + (dice[i][1] * 100)
    else:
        result = max(dice[i])*100

    if result > max_gold:
        max_gold = result

print(max_gold)
