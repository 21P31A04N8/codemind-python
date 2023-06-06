def rev(n):
    k=str(n)
    m=int(k[::-1])
    return m
def prime(n):
    if n<=1:
        return False
    for i in range(2,int((n**0.5)+1)):
        if n%i==0:
            return False
    return True
n=int(input())
r=rev(n)
if prime(n):
    if prime(n) and prime(r):
        print("circular prime")
    else:
        print("prime but not a circular prime")
else:
    print("not prime")