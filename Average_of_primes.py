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
s=0
c=0
for i in range(n):
    if isprime(lst[i]):
        s+=lst[i]
        c+=1
k=s/c
print("{:.2f}".format(k))