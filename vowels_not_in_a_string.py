s=input()
v="aeiou"
l=[]
l1=[]
for i in s:
    if i in v:
        l.append(i)
for i in v:
    if i not in l:
        l1.append(i)
if len(l1)==0:
    print("0")
else:
    print(*l1)