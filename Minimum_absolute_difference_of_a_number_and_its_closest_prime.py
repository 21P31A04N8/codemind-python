def p(n):
    for i in range(2,int(n/2)+1):
        if(n%i==0):
            return 0
    else:
        return 1
n=int(input())
l=[]
for i in range(2,n):
    if(p(i)):
        j=i
for i in range(n,n+100):
    if(p(i)):
        k=i
        break
m=n-j
l.append(m)
n=n-k
l.append(abs(n))
#print(l)
print(min(l))
