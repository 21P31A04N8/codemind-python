for i in range(int(input())):
    n=int(input())
    lst=list(map(int,input().split()))
    l=[]
    for i in range(len(lst)):
        if len(lst)>0:
            m1=max(lst)
            m2=min(lst)
            l.append(m1)
            l.append(m2)
            if len(lst)>1:
                lst.remove(m1)
                lst.remove(m2)
            if len(lst)<=1:
                l=l+lst
                break
    #l.remove(l[len(l)-1])
    print(*l)