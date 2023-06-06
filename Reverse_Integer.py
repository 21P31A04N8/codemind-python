n=int(input())
k=str(n)
n=abs(n)
rev=0
while n!=0:
    r=n%10
    rev=rev*10+r
    n=n//10
if "-" in k:
    print("-"+str(rev))
else:
    print(rev)