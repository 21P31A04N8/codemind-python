a=int(input())
b=int(input())
sum1=0
sum2=0
for i in range(1,(a//2)+1):
    if a%i==0:
        sum1+=i
temp=sum1
for k in range(1,(b//2)+1):
    if (b%k==0):
        sum2+=k
temp1=sum2
if (temp==b and temp1==a):
    print("Amicable")
else:
    print("Not Amicable")