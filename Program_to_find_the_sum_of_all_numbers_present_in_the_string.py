x="0123456789"
s=input()
c=0
for i in s:
    if i in x:
        c+=int(i)
print(c)