#import math
n=int(input())
for i in range(0,int((n)**0.5)+1):
    if (i*(i+1))==n:
        print("YES")
        break
else:
    print("NO")