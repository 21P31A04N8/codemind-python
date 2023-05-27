s=input()
l=[]
l1=[]
for i in s:
    if i=="a" or i=="e" or i=="i" or i=="o" or i=="u" or i=="A" or i=="E" or i=="I" or i=="O" or i=="U":
        l.append(i)
for i in l:
    if i not in l1:
        l1.append(i)
print(*l1)