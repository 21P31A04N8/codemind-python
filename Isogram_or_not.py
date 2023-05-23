n=input()
k=list(n)
k.sort()
l=set(n)
r=list(l)
r.sort()
if r==k:
    print("True")
else:
    print("False")