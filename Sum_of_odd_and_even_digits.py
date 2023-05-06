n=int(input())
l=list(map(int,input().split()))
s=0
s1=0
for i in range(len(l)):
    if i%2==0:
        s+=l[i]
    else:
        s1+=l[i]
c=s-s1
if c==0:
    print("YES")
else:
    print("NO")