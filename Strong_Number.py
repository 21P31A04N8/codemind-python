def fact(n):
    p=1
    while n!=0:
        p=p*n
        n=n-1
    return p
n=int(input())
k=n
q=0
while n!=0:
    r=n%10
    q=q+fact(r)
    n=n//10
if k==q:
    print(f"The number {k} is a strong number")
else:
    print(f"The number {k} is not a strong number")