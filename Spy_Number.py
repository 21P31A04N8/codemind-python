n=int(input())
c=0
pro=1
sum=0
while n!=0:
    rem=n%10
    n=n//10
    sum+=rem
    pro*=rem
if pro==sum:
    print("Spy Number")
else:
    print("Not Spy Number")