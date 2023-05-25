n=int(input())
lst=list(map(int,input().split()))
cnt=0
for i in range(n):
    for j in range(n):
        if lst[i]==lst[j] and lst[i]!=0 and lst[j]!=0 and i!=j:
            cnt+=1
            lst[i]=0
            lst[j]=0
print(cnt)