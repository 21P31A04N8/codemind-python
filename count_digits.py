def digit(n):
    n=abs(n)
    k=str(n)
    return len(k)
n=int(input())
lst=list(map(int,input().split()))
l=[]
for i in range(n):
    m=digit(lst[i])
    l.append(m)
print(*l)