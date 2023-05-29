n=input().lower()
k=list(n)
l=[]
for i in k:
    if i!=" ":
        l.append(i)
l.sort()
#print(*l)
#for i in range(len(l)):
k=set(l)
print(len(k))