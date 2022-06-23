def dfs(n):
    print(n,end=" ")
    vi[n]=True
    for i in (temp[n]):
        if not vi[i]:
            dfs(i)

def bfs(n):
    vi[n] = True
    queue = deque([n])
    while queue:
        v = queue.popleft()
        print(v, end= ' ')
        for i in temp[v]:   
            if not vi[i]:
                queue.append(i)
                vi[i] = True


from collections import deque
n,m,v = map(int,input().split())
temp = [[] for _ in range(n+1)]
vi = [False]*(n+1)
for i in range(0,m):
    x, y = map(int,input().split())
    temp[x].append(y)
    temp[y].append(x)

for i in range(1,n+1):
    temp[i].sort()

dfs(v)
vi = [False]*(n+1)
print()
bfs(v)
