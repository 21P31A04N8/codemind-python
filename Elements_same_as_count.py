n=int(input())
lst=list(map(int,input().split()))
c=0
for i in sorted(set(lst),key=lst.index):
    if lst.count(i)==i:
        print(i,end=" ")
        c+=1
if c==0:
    print("-1")

