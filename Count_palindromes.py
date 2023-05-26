def palin(n):
    k=str(n)
    m=k[::-1]
    if int(m)==n:
        return True
    else:
        return False
n=int(input())
lst=list(map(int,input().split()))
cnt=0
for i in range(n):
    if palin(lst[i]):
        cnt+=1
print(cnt)   