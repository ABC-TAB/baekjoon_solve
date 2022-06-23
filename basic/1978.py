lop = int(input())
a = []
con =0
a = input().split()
a = list(map(int,a))
for i in range(0,lop):
    if a[i]==1:
        temp =1
    else:
        temp=0
    for j in range(2,a[i]-1):
        if a[i]%j ==0:
            temp +=1
        if temp > 0 :
            continue
    if temp ==0:
        con +=1
print (con)
