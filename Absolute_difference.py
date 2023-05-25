def prime(n):
    for i in range(2,(n//2)+1):
        if (n%i==0):
            return 0
    else:
        return 1
n=int(input())
lst=list(map(int,input().split()))
p=1
p1=1
for i in range(n):
    if prime(lst[i]):
        p=p*lst[i]
    else:
        p1=p1*lst[i]
#print(p)
#print(p1)
print(abs(p1-p))