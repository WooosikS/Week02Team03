import sys
input = sys.stdin.readline

stack = []  # stack 갯 용 리스트
result = []  # 정답 을 담아둘 리스트

while True:
    arr = list(map(int, input().split()))

    if arr[0] == 0:
        break

    total = arr[0]  # 처음에는 리스트 갯수를 알려주는 숫자이기 때문에 리스트에서 제외
    arr = arr[1:]  # 처음 숫자는 필요 없으니 뺀 숫자들로 리스트를 재구성
    tem = []  # 높이 값을 저장하기 위해 만든 빈 리스트

    for i in range(len(arr)):
        cut = i  # 인덱스 값을 저장하기 위한 변수

        # 스택이 비어있지 않고, 비교하는 탑의 높이가 지금 직사형의 높이 ( stack에 저장된 값 ) 보다 작다면
        while stack and stack[-1][0] > arr[i]:
            # 스택에서 pop 하여 값을 가져온다
            height, index = stack.pop()
            # tem에 높이 값을 저장한다.
            tem.append(height * (i - index))
            #
            cut = index
        # 처리 후 스택에 저장
        stack.append((arr[i], cut))
    # 끝까지 순회하고도 스택이 비지 않았다면
    while stack:
        height, index = stack.pop()
        tem.append(height * (total - index))
    # 높이 저장 중 가장 큰 값을 정답배열에 저장
    result.append(max(tem))

# 정답 출력
for i in result:
    print(i)
