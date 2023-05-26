def wave(x,l):
    c=0
    if l[0]<l[1]:
        for i in range(1,x-1,2):
            if (l[i-1]<l[i] and l[i]>l[i-1]):
                c+=1
            else:
                c=0
                return 0
                break
        if c!=0:
            return 1
    else:
        for i in range(1,x-1,2):
            if (l[i-1]>l[i] and l[i]<l[i-1]):
                c+=1
            else:
                c=0
                return 0
                break
        if c!=0:
            return 1
x = int(input())
l = list(map(int,input().split()))
if wave(x,l):
    print("yes")
else:
    print("no")
