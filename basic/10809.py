import string

st = input()
a = list(string.ascii_lowercase)
b = [-1]*26
c = list(st)
cnt = 0
for i,j in enumerate(c):
    for k in range(0,26):
        if j == a[k]:
            if b[k]==-1:
                b[k] = cnt
            break
    cnt +=1

for l in range(26):
    print(b[l],end=" ")            