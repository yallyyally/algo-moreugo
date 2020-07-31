#정다면체
#정N면체 주사위와 정M면체 주사위 두개르 나올 수 있는 눈의 합 중 가장 확률이 높은 수 출력
#여러개일 경우 오름차순으로 출력.
#머리굴리지 말고 있는 그대로 생각하자.

N,M = map(int,input().split())
#작거나 같은수 ->N,큰수 ->M으로 메핑
# ans=[]
if M<=N:
    M,N=N,M
    # M=N
    # N=M -> X

cnt=[0]*(N+M+3)

#i - N면체, j-M면체
#일단 다 계산하기->인덱스에 넣기
for i in range(1,N+1):
    for j in range(1,M+1):
        cnt[i+j] +=1

max=0
#최대 cnt 찾기
for i in range(N+M+1):
    if cnt[i]>max:
        max=cnt[i]

#최대 cnt에 해당하는것 출력하기
for i in range(N+M+1):
    if cnt[i]==max:
        print(i,end=' ')

