n=input().lower()
m=input().lower()
s=''
for i in n:
    if i in m and i not in s and i!=" ":
        s+=i
#for i in m:
 #   if i in n and i not in s and i!=" ":
  #      s+=i
#s=s.replace(" ","")
if len(s)==0:
    print("-1")
else:
    for i in sorted(s):
        print(i,end='')