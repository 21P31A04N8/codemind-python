import math
n = int(input())
count_digits = len(str(n))
sum = 0 
x = n
while (x!=0) :
    r = x % 10
    sum = (int) (sum + math.pow(r, count_digits))
    count_digits = count_digits - 1
    x = x//10
if (sum==n) :
    print ("True")
else :
    print ("False")