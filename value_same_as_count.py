n=int(input())
lst=list(map(int,input().split()))
c=0
for i in sorted(set(lst)):
    if lst.count(i)==i:
        c+=1
print(c)