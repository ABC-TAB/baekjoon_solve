import sys

a = int(sys.stdin.readline())
b = []
for i in range(0,a):   
    b.append(int(sys.stdin.readline()))
b.sort()
for i in range(0,a):   
    print(b[i])