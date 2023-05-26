n=int(input())
l=list(map(int,input().split()))
k=int(input())
lst=[]
cnt=0
for i in range(n):
    if l.count(l[i])==k:
        lst.append(l[i])
        #print(i,end=" ")
        #print(l.count(l[i]))
    else:
        cnt+=1
s=set(lst)
if cnt==len(l):
    print("-1")
else:
    print(*s)