import math
n=int(input())
cnt=0
for i in range(1,(n//2)):
    if math.sqrt(n)==i:
        cnt=1
    else:
        cnt=cnt
if cnt==0:
    print(False)
else:
    print(True)