def fun(s):
    v=0
    for i in s:
        if i in "aeiouAEIOU":
            v+=1
    return v
s=input()
k=s.split()
l=[]
for i in k:
    k=fun(i)
    l.append(k)
print(l.count(max(l)))