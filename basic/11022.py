
cont = int(input())
hap = []
list_a = []
list_b = []

for i in range(cont):
    a, b =map(int, input().split())
    list_a.append(a)
    list_b.append(b)
    hap.append(a+b)
j=0
for i in hap:
    j+=1
    print(f"Case #{j}:",list_a[j-1],"+",list_b[j-1],"=",i)
