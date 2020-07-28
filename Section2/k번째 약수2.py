#k번째 약수 찾기
#두개의 자연수 N과 K가 주어졌을 때, N의 약수들 중 K번째로 작은 수를 출력하는 프로그램을 작성하시오.
##K번째 약수가 존재하지 않을 경우엔 -1 출력
import sys
# sys.stdin=open("input.txt","rt")
N,K = map(int,input().split())
#약수의 개수
cnt=0
for i in range(1,N+1):
    if N%i==0:
        cnt+=1
    if cnt==K:
        print(i)
        break
else:
    print(-1)
    #for문 중간에 break 당하지 않고 정상적으로 끝났을 경우



