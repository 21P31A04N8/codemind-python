import math
a,b,c=map(int,input().split())
n=math.pow(a,b)
m=n%c
print(int(m))