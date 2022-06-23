a = input()
b = [3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 10, 10, 10, 10]
a = list(a.upper())
cnt = 0

for i in range(0,len(a)):
    cnt = cnt + (b[ord(a[i])-65])
print(cnt)
