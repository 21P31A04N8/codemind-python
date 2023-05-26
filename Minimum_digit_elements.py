def digit(n):
    n=abs(n)
    k=str(n)
    return len(k)
n=int(input())
lst=list(map(int,input().split()))
l=[]
cnt=0
for i in range(n):
    m=digit(lst[i])
    l.append(m)
b=min(l)
#print(l)
for i in range(n):
    if digit(lst[i])==b:
        cnt+=1
print(cnt)