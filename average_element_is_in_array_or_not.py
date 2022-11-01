n=int(input())
a=list(map(int,input().split()))
sum=0
cnt=0
for i in range(0,n):
        sum+=a[i]
avg=sum//n
for i in range(0,n):
    if(a[i]==avg):
        cnt+=1
if(cnt>0):
    print("True")
else:
    print("False")