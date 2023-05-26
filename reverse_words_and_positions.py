k=input()
lst=k.split()
l1=[]
for i in range(len(lst)):
    m=lst[i]
    k=m[::-1]
    l1.append(k)
l2=l1[::-1]
print(*l2)