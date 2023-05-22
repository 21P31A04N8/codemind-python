n=int(input())
lst=list(map(int,input().split()))
cnt=0
s=0
es=0
for i in range(n//2):
    s+=lst[i]
    cnt+=1
for i in range(cnt,n):
    es+=lst[i]
print(s)
print(es)