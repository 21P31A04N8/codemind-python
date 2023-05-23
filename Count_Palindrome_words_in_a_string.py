def palin(s):
    k=s.lower()
    n=k[::-1]
    if n==k:
        return True
    else:
        return False
lst=list(map(str,input().split()))
cnt=0
for i in lst:
    if palin(i):
        cnt+=1
print(cnt)