for i in range(int(input())):
    n=int(input())
    p=1
    while n!=0:
        p=p*n
        n=n-1
    print(p)