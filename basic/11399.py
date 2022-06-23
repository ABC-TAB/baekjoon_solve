import sys
a = int(sys.stdin.readline())
t = []
hap = 0
hap1 = 0
t = input().split()
t = list(map(int,t))
t.sort()


for i in range(0,len(t)):
    hap = hap + t[i]
    hap1 = hap1 + hap


print(hap1)