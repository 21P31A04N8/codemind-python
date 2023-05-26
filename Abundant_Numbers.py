n=int(input())
l1=[]
for i in range(2,(n//2)+1):
    if n%i==0:
        l1.append(i)
k=sum(l1)
if k>n:
    print("True")
else:
    print("False")