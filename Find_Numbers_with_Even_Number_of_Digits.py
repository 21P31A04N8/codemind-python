def digit(n):
    k=str(n)
    l=len(k)
    return l
n=int(input())
lst=list(map(int,input().split()))
cnt=0
for i in range(n):
    r=digit(lst[i])
    if r%2==0:
        cnt+=1
print(cnt)