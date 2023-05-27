s=input()
k="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
m=list(s)
c=0
for i in m:
    i=i.strip()
    if i not in k:
        c+=1
print(c)