arr = input()

stack = []
res = 0
tmp = 1

for i in range(len(arr)):

    if arr[i] == "(":
        stack.append(arr[i])
        tmp *= 2

    elif arr[i] == "[":
        stack.append(arr[i])
        tmp *= 3

    elif arr[i] == ")":

        if not stack or arr[-1] == "[":
            res = 0
            break
        if arr[i-1] == "(":
            res += tmp
        stack.pop()
        tmp //= 2

    else:
        if not stack or arr[-1] == "(":
            res = 0
            break
        if arr[i-1] == "[":
            res += tmp
        stack.pop()
        tmp //= 3

if stack:
    res = 0

print(res)
