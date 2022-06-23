c = []
while 1:
    a, b =map(int, input().split())

    if a == 0 and b==0:
        break
    c.append(a+b)

for i in c:
    print(i)