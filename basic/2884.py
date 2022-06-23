h, m =map(int, input().split())

hh = h
mm = m

if (m-45) < 0 :
    if (h-1)<0:
        h= (h+24)-1
    else:
        h = h - 1

    m = (m+60)-45     
else:
    m = m-45

print(h ,m)