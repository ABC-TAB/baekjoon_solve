from operator import truth


def solve(a):
    ans = 0
    a = list(map(int,a))
    for i in range(0,len(a)):
        ans = ans + a[i]
    return ans

a=[1,2,3,4,7,8,9]
print(solve(a))

