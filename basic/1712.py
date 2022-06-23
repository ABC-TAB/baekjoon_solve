a,b,c = map(int,input().split())
d = c
cnt =1 
if c > b:
    cnt = int(a / (d-b))
d = d* cnt
a = a +(b*cnt)
while 1:
    if c <= b:
        print(-1)
        break

    if a>=d:
        a = a + b
        d = d + c
        cnt = cnt +1
    else:
        print(cnt)
        break




