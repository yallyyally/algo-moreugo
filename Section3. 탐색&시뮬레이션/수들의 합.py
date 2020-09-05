N,M= map(int,input().split())
#N개의 수열 의 합이 M이 되는 경우의 수 구하기
list=list(map(int,input().split()))
i,j = 0,0 #i는 시작점 j는 확장점
num = []
sum = 0
ans=0
flag = 0 #break
for i in range(N):
    for j in range(i,N):
        num.append(list[j])
        sum+=list[j]
        if sum==M:
            ans+=1
            sum-=num[0]
            num.pop(0)
            if j==N-1:
                flag=1
            break
        elif sum>M: #sum>M:
            sum-=num[0]
            num.pop(0)
            break
        else: #sum<M
            if j==N-1:
                flag=1
                break
    if flag:
        break
    num.clear()
    sum=0

print(ans)