for i in range(int(input())):
    n=int(input())
    p=list(map(int,input().split()))
    q=list(map(int,input().split()))
    s=set(p+q)
    lst=list(s)
    l=[]
    for i in range(1,n+1):
        l.append(i)
    for i in lst:
        l.remove(i)
    if len(l)==0:
        print("YES")
    else:
        print("NO")