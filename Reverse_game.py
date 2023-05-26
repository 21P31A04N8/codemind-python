def rev(n):
    re=0
    while n!=0:
        r=n%10
        re=re*10+r
        n=n//10
    return re
n=int(input())
lst=list(map(int,input().split()))
l=[]
for i in range(n):
    k=rev(lst[i])
    l.append(k)
print(*l)