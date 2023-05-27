s=input()
k=input()
lst=list(s)
n=len(lst)
cnt=0
while n!=0:
    if k in s:
        print(True)
        cnt=1
        break
    n-=1
else:
    print(False)
if cnt==1:
    print(lst.index(k))