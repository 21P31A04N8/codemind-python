n=int(input())
a=list(map(int,input().split()))
x=int(input())
cnt=0
for i in range(0,n):
    if(a[i]==x):
        cnt+=1
        break
if cnt==1:
    print("True")
else:
    print("False")
