n=input()
c=0
for i in n:
    if i=="U" or i=="R":
        c+=1
    else:
        c-=1
if c==0:
    print("True")
else:
    print("False")