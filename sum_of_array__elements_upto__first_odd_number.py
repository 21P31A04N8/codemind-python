n=int(input())
lst=list(map(int,input().split()))
s=0
for i in range(n):
    if lst[i]%2==1:
        break
    s+=lst[i]
print(s)