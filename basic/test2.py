def dfs(n):
    print(n,end=" ")
    vi[n]=True
    for i in temp[n]:
        if not vi[i]:
            dfs(i)


def bfs(n):
    vi[n] = True
    queue = deque([n])
    while queue:
        v = queue.popleft()
        #print(v, end= ' ')
        for i in temp[v]:
            print(i,end=' ')   
            if not vi[i]:
                queue.append(i)
                vi[i] = True
                


from collections import deque                
temp = [[], [2, 3, 4], [1, 4], [1, 4], [1, 2, 3]]
vi = [False]*(5+1)

bfs(1)

print(temp)
