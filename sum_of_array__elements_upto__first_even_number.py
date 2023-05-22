n=int(input())
lst=list(map(int,input().split()))
s=0
for i in range(len(lst)):
    if lst[i]%2==0:
        break
    s+=lst[i]
print(s)