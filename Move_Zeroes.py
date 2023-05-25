n=int(input())
lst=list(map(int,input().split()))
l=[]
l1=[]
for i in range(n):
    if lst[i]!=0:
        l.append(lst[i])
    else:
        l1.append(lst[i])
print(*l,*l1)