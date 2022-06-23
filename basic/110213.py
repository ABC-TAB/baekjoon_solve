cont = int(input())
hap = []
for i in range(cont):
    a, b =map(int, input().split())
    hap.append(a+b)
j=0
for i in hap:
    j+=1
    print(f"Case #{j}:",i)
