k=input()
lst=k.split()
l1=[]
for i in range(len(lst)):
    if i%2==0:
        m=lst[i]
        k=m[::-1]
        l1.append(k)
    else:
        l1.append(lst[i])
print(*l1)