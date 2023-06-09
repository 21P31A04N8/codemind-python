for i in range(int(input())):
    n=int(input())
    lst=list(map(int,input().split()))
    cnt=0
    for i in range(len(lst)):
        k=lst[i]
        for j in range(i+1,len(lst)):
            s=k+lst[j]
            if s in lst:
                cnt+=1
    if cnt==0:
        print("-1")
    else:
        print(cnt)
                