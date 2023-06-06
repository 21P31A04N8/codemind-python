for i in range(int(input())):    
    def palin(n):
        k=str(n)
        m=k[::-1]
        if k==m:
            return True
        else:
            return False
    n=int(input())
    if palin(n):
        print("True")
    else:
        print("False")