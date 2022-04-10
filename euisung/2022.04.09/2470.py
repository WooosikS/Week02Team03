n = int(input())
arr = list(map(int, input().split()))
arr.sort
center = (0 + n)//2
start = 0
end = n-1
maxi = 2170000

while start < end:
    tem = arr[start] + arr[end]
    result = abs(tem)

    if maxi > result :
        maxi = result
        
