s=input()
v="aeiou"
cnt=0
l=[]
for i in s:
   if i in v:
       l.append(i)
k=set(l)
if len(k)==len(v):
    print("True")
else:
    print("False")