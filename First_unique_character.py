n=input().lower()
k=list(n)
l=[]
for i in k:
    if k.count(i)==1 and i!=" ":
        l.append(i)
#l.sort()
#print(*l)
#for i in range(len(l)):
if len(l)==0:
    print("-1")
else:
    print(l[0])