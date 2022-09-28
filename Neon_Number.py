n=int(input())
c=0
sum=0
pro=n*n
while pro!=0:
    rem=pro%10
    sum+=rem
    pro=pro//10
    c+=1
if sum==n:
    print("Neon Number")
else:
    print("Not Neon Number")
    
    