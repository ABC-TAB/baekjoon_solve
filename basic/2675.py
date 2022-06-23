a = int(input())

for i in range(0,a):
    re , val = input().split()
    val = list(val)
    re = int(re)
    for j in range(0,len(val)):
        for k in range(0,re):
            print(val[j],end="")
    print()