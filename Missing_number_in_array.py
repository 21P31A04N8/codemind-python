for i in range(int(input())):
    n=int(input())
    lst=list(map(int,input().split()))
    s=0
    for i in range(1,n+1):
        s+=i
    s1=sum(lst)
    print(s-s1)