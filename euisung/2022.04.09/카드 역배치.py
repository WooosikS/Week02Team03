card = list(range(21))

for _ in range(10):
    start, end = map(int, input().split())
    for i in range((end - start + 1)//2):
        card[start+i], card[end-i] = card[end-i], card[start+i]
card.pop(0)
for x in card:
    print(x, end=' ')
