arr = []

while 1:
    try:
        a, b =map(int, input().split())
        arr.append(a+b)
    except:
        break  
    
for i in arr:
    print(i)


