a = ['1']*10
a = map(int,a) # Python 2.x
print(a) # 출력 : <map object at 0x04D280F0>

a = list(map(int,a)) # Python 3.x
print(a) # 출력 : [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
