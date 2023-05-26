n=int(input())
s=str(n)
lst=list(s)
k=set(s)
if len(lst)==len(k):
    print("Unique Number")
else:
    print("Not Unique Number")
