for i in range(int(input())):
    n=int(input())
    for i in range((n//2)+1):
        if i*i==n:
            print("True")
            break
    else:
        print("False")