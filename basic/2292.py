target = int(input())
con =1
a = 1
s = 6
while 1:
    if target>a:
        a = a + s
        s = s+6
        con +=1
    else:
        print(con)
        break