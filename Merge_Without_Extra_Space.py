for i in range(int(input())):
    a,b=map(int,input().split())
    l1=list(map(int,input().split()))
    l2=list(map(int,input().split()))
    l3=l1+l2
    l3.sort()
    print(*l3)