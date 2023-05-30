n=input()
r=input()
k=list(n)
if r not in k:
    print("-1")
else:
    print(k.count(r))