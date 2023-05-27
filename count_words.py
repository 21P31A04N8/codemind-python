s=input()
k="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
l=s.split()
c=0
for i in l:
    i=i.strip()
    n=i[0]
    r=i[::-1]
    if n in "aeiouAEIOU" and r[0] in k:
        c+=1
print(c)