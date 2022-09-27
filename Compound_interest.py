p,r,t=map(int,input().split())
cp = p * (pow((1 + r / 100), t))
a=("{:.2f}".format(cp))
print(a)