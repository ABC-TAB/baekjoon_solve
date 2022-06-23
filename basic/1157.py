import string

st = input()
a = list(string.ascii_lowercase)
b = [0]*26
st = st.lower()
c = list(st)
for i in range(0,len(c)):
    for j in range(0,26):
        if c[i] == a[j]:
            b[j] += 1
            

M = max(b)
cnt = 0
for i in range(0,26):
    if M == b[i]:
        cnt +=1
    if cnt > 1:
        print ("?")
        break

if cnt==1:
    print(a[b.index(max(b))].upper())
