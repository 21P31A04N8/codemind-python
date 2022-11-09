n=int(input())
arr=list(map(int,input().split()))
cnt=0
for i in range(len(arr)-2):
    if arr[i]%2==0 and arr[i+1]%2==1 and arr[i+2]%2==0:
        cnt+=1
print(cnt)