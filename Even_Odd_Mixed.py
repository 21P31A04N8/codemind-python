n=int(input())
l=len(str(n))
cnt,cnt1=0,0
while n!=0:
    r=n%10
    n=n//10
    if r%2==0:
        cnt+=1
    else:
        cnt1+=1
if l==cnt:
    print("Even")
elif l==cnt1:
    print("Odd")
else:
    print("Mixed")