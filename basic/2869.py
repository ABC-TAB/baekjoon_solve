A, B, V = map(int,input().split())
UP = 0
cnt = 1
'''
while 1:
    cnt = cnt + 1
    UP = UP + A
    if UP >= V:
        print(cnt)
        break
    else:
        UP = UP - B
'''
V = V - A
if V%(A-B)==0:
    temp = V/(A-B)
else:
    temp = V/(A-B)+1
print(temp)
cnt = cnt + temp
cnt = int(cnt)
print(cnt)