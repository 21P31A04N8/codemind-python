def perf(n):
    p=n**0.5
    if n%p==0:
        return True
    else:
        return False
n=int(input())
lst=list(map(int,input().split()))
s=0
for i in range(n):
    if perf(lst[i]):
        s+=lst[i]
print(s)
        