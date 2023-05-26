def p(n):
    for i in range(2,int(n/2)+1):
        if(n%i==0):
            return 0
    else:
        return 1
def palin(n):
    k=str(n)
    m=k[::-1]
    if int(m)==n:
        return True
    else:
        return False
n=int(input())
for i in range(n+1,999999):
    if p(i) and palin(i):
        print(i)
        break