n=int(input())
l=str(n)
k=list(l)
m=len(k)
if m==10 and k[0]!=0:
    print("Valid")
else:
    print("Invalid")