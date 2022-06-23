N = int(input())
cnt = N  # 결과는 N개

for i in range(N):
    word = input()
    for j in range(0, len(word)-1):
        if word[j] == word[j+1]:  # 현재 원소가 다음 원소와 같을 때(연속)
            pass
        elif word[j] in word[j+1:]:  # 현재 원소가 다음 원소 뒤에 또 존재할 때(불연속)
            cnt -= 1
            break

print(cnt)



'''
cnt = int(input())
res=0
for i in range(0,cnt):
    a = input().lower()
    b = list(a)
    sw = 1
    for j in range(0,len(b)):
        for k in range(j+2,len(b),1):
            if a[j]==a[k]:
                if a[j]==a[k-1]:
                    sw=1
                else:
                    sw=0
                    break
        if sw==0:
            break
    if sw==1:
        res +=1

print(res)
'''