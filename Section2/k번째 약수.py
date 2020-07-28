#k번째 약수 찾기
#두개의 자연수 N과 K가 주어졌을 때, N의 약수들 중 K번째로 작은 수를 출력하는 프로그램을 작성하시오.
##K번째 약수가 존재하지 않을 경우엔 -1 출력
import sys
# sys.stdin=open("input.txt","rt")
N,K = map(int,input().split())
#약수의 개수
yaksu=[]

#1~자기 자신까지 일단.
for i in range(1,N+1):
    #약수일 경우 리스트에 추가
    if N%i==0:
        yaksu.append(i)

#K번째 찾기.
if len(yaksu)<K:
    print(-1)
else:
    print(yaksu[K-1])



