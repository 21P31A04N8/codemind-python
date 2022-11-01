n=int(input())
a=list(map(int,input().split()))
sum=0
for i in range(0,n):
    if(i%2==1):
        sum+=a[i]
print(sum)