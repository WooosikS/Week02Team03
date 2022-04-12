# import sys

# num = int(sys.stdin.readline())
# count = 0

# queue_list = []
# for _ in range(num):
#     command = list(sys.stdin.readline().split())
#     if command[0] =='push':
#         queue_list.append(command[1])
#     elif command[0] == 'pop':
#         if len(queue_list) > count:
#             print(queue_list[count])
#             count += 1
#         else:
#             print(-1)
#     elif command[0] == 'size':
#         print(len(queue_list)-count)
#     elif command[0] == 'empty':
#         if len(queue_list) == count:
#             print(1)
#             count = 0
#             queue_list = []
#         else:
#             print(0)
#     elif command[0] == 'front':
#         if len(queue_list) > count:
#             print(queue_list[count])
#         else:
#             print(0)
#     elif command[0] == 'back':
#         if len(queue_list) > count:
#             print(queue_list[-1])
#         else:
#             print(-1)





# from sys import stdin
# input()
# s, com= [], stdin.readlines()
# cnt = 0
# for x in com:
#     c = x.split()
#     if c[0] == "push":
#         s.append(c[1])
#     elif c[0] == 'pop':
#         if len(s) > cnt:
#             print(s[cnt])
#             cnt += 1
#         else: print(-1)
#     elif c[0] == 'size':
#         print(len(s)-cnt)
#     elif c[0] == 'empty':
#         if len(s) == cnt :
#             print(1)
#             cnt = 0
#             s = []
#         else: print(0)
#     elif c[0] == 'front':
#         if len(s) > cnt: print(s[cnt])
#         else: print(-1)
#     elif c[0] == 'back':
#         if len(s) > cnt: print(s[-1])
#         else: print(-1)








import sys
from collections import deque

num = int(sys.stdin.readline())
q = deque([])

for _ in range(num):
    q_list = list(sys.stdin.readline().split())
    if q_list[0] == "push":
        q.append(q_list[1])
    elif q_list[0] == "pop":
        if not q:
            print(-1)
        else:
            print(q.popleft())
    elif q_list[0] == "size":
        print(len(q))
    elif q_list[0] == "empty":
        if not q:
            print(1)
        else:
            print(0)
    elif q_list[0] == "front":
        if not q:
            print(-1)
        else:
            print(q[0])
    elif q_list[0] == "back":
        if not q:
            print(-1)
        else:
            print(q[-1])