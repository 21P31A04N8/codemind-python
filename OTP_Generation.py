n=input()
s=""
for i in n:
    if int(i)%2==1:
        k=int(i)*int(i)
        s+=str(k)
    else:
        continue
print(s)