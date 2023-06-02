s1=input().strip()
s2=input().strip()
l=list(s1)+list(s2)
l.sort()
for i in range(len(l)):
    print(l[i],end="")
#print(l)