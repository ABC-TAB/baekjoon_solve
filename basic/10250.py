guest = int(input())
for i in range(1,guest+1):
    x, y, n = map(int,input().split())
    temp = n%x # 나머지
    mok = int(n/x)+1
    if temp == 0:
        temp = x
        mok = int(n/x)
    if mok >=10:
        print(f'{temp}{mok}')
    else:
        print(f'{temp}0{mok}')
#6 12 7
#201