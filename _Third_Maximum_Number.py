n=int(input())
lst=list(map(int,input().split()))
if len(lst)<=2:
    print(max(lst))
else:
    s=set(lst)
    l1=list(s)
    m1=max(l1)
    l1.remove(m1)
    m2=max(l1)
    l1.remove(m2)
    print(max(l1))
    