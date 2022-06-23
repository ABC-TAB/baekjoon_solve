import sys
cnt = int(input())
stack = []

for i in range(0,cnt):
    a = sys.stdin.readline()
    a = a.split()
    if a[0] == "push":
        stack.append(a[1])
    if a[0] == "pop":
        if len(stack)==0:
            print(-1)
        else:
            print(stack[-1])
            stack.pop()
    if a[0] == "top":
        if len(stack)==0:
            print(-1)
        else:
            print(stack[-1])
    if a[0] == "size":
        print(len(stack))
    if a[0] == "empty":
        if len(stack)==0:
            print(1)
        else:
            print(0)
       