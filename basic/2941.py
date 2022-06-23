
a=['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
ch=[False]*8
b =input()
i = 0
cnt=0

while i<8 :
    if a[i] in b:
        cnt+=1
        b=b.replace(a[i],' ',1)
        ch[i]=True
        i=0
    else :
        i+=1

b=b.replace(' ','')
b=b.replace('-','')
b=b.replace('=','')

cnt = cnt + len(b)
print(cnt)