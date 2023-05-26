def digit(n):
    n=abs(n)
    k=str(n)
    return len(k)
n,k=map(int,input().split())
lst=list(map(int,input().split()))
cnt=0
for i in range(n):
    if digit(lst[i])==k:
        cnt+=1
print(cnt)