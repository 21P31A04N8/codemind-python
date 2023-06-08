n=int(input())
lst=list(map(int,input().split()))
l=[]
l1=[]
for i in range((n//2)):
    l.append(lst[i])
for i in range(n//2,n):
    l1.append(lst[i])
k=l1[::-1]
new=k+l
print(*new)
    