l1=list(map(int,input().split()))
l2=list(map(int,input().split()))
cnt=cnt1=0
for i in range(len(l1)):
    if l1[i]>l2[i]:
        cnt+=1
    elif l1[i]<l2[i]:
        cnt1+=1
print(cnt,cnt1)