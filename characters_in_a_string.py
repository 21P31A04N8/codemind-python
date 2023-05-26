k=input()
l=list(k)
l1=[]
for i in range(len(l)):
    m=len(str(l[i]))
    l1.append(m)
print(sum(l1))