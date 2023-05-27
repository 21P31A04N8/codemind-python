s=input()
k="abcdefghijklmnopqrstuvwxyz"
m=list(s)
c=0
for i in m:
    #i=i.strip()
    if i in k:
        c+=1
print(c)