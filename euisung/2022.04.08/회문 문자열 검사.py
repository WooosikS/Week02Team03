n = int(input())

for i in range(n):
    word = input()
    word_up = word.upper()
    if word.upper() == word_up[::-1]:
        print("#%d YES" % (i+1))
    else:
        print("#%d NO" % (i+1))
