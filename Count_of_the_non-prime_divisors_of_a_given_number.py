n=int(input())
cnt=0
for i in range(2,(n+1)):
    if n%i==0:
        for j in range(2,(i//2)+1):
            if i%j==0:
                cnt+=1
                break
print(cnt+1)
        