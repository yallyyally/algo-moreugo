#정다면체
#정N면체 주사위와 정M면체 주사위 두개르 나올 수 있는 눈의 합 중 가장 확률이 높은 수 출력
#여러개일 경우 오름차순으로 출력.

N,M = map(int,input().split())
#작거나 같은수 ->N,큰수 ->M으로 메핑
ans=[]
if M<=N:
    M,N=N,M
    # M=N
    # N=M -> X

max=-21470000

for x in range(2,N+M+1):
    cnt=0
    for y in range(1,N+1):
        if x-y<=M and x-y>=1:
            cnt += 1

    if cnt>max:
            ans.clear()
            ans.append(x)
            max=cnt
    elif cnt==max:
            ans.append(x)

for x in ans:
    print(x,end=' ')