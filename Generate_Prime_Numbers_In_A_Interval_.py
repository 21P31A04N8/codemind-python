def prime(n):
    if n<=1:
        return False
    for i in range(2,(n//2)+1):
        if n%i==0:
            return False
    return True
n=int(input())
m=int(input())
#print(n,m)
for i in range(n,m+1):
    if prime(i):
        print(i)