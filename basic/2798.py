a = input().split()
a = list(map(int,a))
b=input().split()
b = list(map(int,b))
temp = 0
sum=0
for i in range(0,a[0]-2):
    for j in range(i+1,a[0]-1):
        for k in range(j+1,a[0]):
            sum = b[i]+b[j]+b[k]
            if a[1] == sum:
                temp = sum
                break
            elif a[1] >= sum :
                if temp < sum:
                    temp = sum

print(temp)

