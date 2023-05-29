for i in range(int(input())):
    n=int(input())
    p=[]
    while n!=0:
        r=n%10
        n=n//10
        p.append(r)
    c=0
    j=min(p)
    for i in range(min(p),max(p)+1):
        if j in p:
            c+=1
            #print(i)
            j+=1
    #print(p)
    if c==len(p):
        print("YES")
    else:
        print("NO")