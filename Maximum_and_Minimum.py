n=int(input())
l=list(map(int,input().split()))
lst=[]
cnt=0
for i in range(n):
    if l.count(l[i])==l[i]:
        lst.append(l[i])
        #print(i,end=" ")
        #print(l.count(l[i]))
    else:
        cnt+=1
s=set(lst)
r=list(s)
if cnt==len(l):
    print("-1")
else:
    print(min(r),max(r))