n=int(input())
lst=list(map(int,input().split()))
l=[]
l1=[]
for i in range(n):
    k=lst.count(lst[i])
    l.append(k)
m=max(l)
for i in lst:
    #if m!=1:
    if lst.count(i)==m:
        l1.append(i)
#else:
 #   print("0")
print(min(l1))