cnt = int(input())
a = []
for i in range(0,cnt):
    a = input()
    a = list(a)
    sw= 0
    for j in range(0,len(a)):
        if sw <0:
            break
        elif a[j] =="(":
            sw += 1
        else:
            sw -= 1
    if sw==0:
        print("YES")
    else:
        print("NO")
