n=int(input())
lst=list(map(int,input().split()))
c=0
for i in range(1,n-1):
    if lst[i-1]+lst[i]==lst[i+1]:
        c+=1
    else:
        c=0
        break
if c!=0:
    print("yes")
else:
    print("no")