k=input()
lst=k.split()
l1=[]
for i in range(len(lst)):
    r=lst[i]
    m=r[::-1]
    l1.append(m)
print(*l1)
