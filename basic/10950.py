ct =int(input())
list= []
for i in range(ct):
    a, b =map(int, input().split())
    list.append(a+b)

for i in list:
    print(i)
