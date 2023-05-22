def isprime(n):
    cnt=0
    for i in range(1,n+1):
        if n%i==0:
            cnt+=1
        else:
            cnt=cnt
    if cnt==2:
        return True
    else:
        return False
n=int(input())
lst=list(map(int,input().split()))
k=int(input())
c=0
for i in range(n):
    if isprime(lst[i]):
        if lst[i]<=k:
            c+=1
print(c)