n=input().lower()
k=list(n)
for i in k:
    if k.count(i)==1 and i.isalpha:
        print(k.index(i))
        break
else:
    print("-1")