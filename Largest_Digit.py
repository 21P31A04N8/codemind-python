n=int(input())
large=0
rem=0
while n>0:
    rem=n%10
    if rem>large:
        large=rem
    n=n//10
print("%d"%large)