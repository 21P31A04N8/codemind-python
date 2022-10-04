n=int(input())
temp=n
s=0
while n:
    k=n%10
    n=n//10
    s=s*10+k
if temp==s:
    print("True")
else:
    print("False")