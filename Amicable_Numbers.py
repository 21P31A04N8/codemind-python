n=int(input())
m=int(input())
sn=0
sm=0
for i in range(1,(n//2)+1):
    if n%i==0:
        sn+=i
for i in range(1,(m//2)+1):
    if m%i==0:
        sm+=i
if sn==m and sm==n:
    print("Amicable")
else:
    print("Not Amicable")