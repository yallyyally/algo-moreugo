#k번째 큰 수
#N개의 자연수 카드가 있을 때,(중복 가능) 이중 3장의 합을 가능한 모든 경우의 수 다 기록할 경우
#중복제거 자료구조 ->""set""!!


N,K = map(int,input().split())
cards=list(map(int,input().split()))
sums=[]

# for i in range(N-3): #0~N-1
#     sum=0
#     for j in range(3):
#         sum += cards[i+j]
#     sums.append(sum)
#이코드의 문제점 -> 이웃하는 것들만 고려,,

for i in range(N):
    for j in range(i+1,N):
        for k in range(j+1,N):
            sums.append(cards[i]+cards[j]+cards[k])

sums.sort()
sums.reverse()
cnt=1
#변수 하나 더 설정 -> 메모리 낭비

for i in range(len(sums)):
    #중복 제거.
    if i!=0:
        if sums[i]!=sums[i-1]:
            cnt+=1
    if(cnt==K):
        break
        #이거 안해주고 그냥 여기서 print만 시키면 시간초과 에러남.
print(sums[i])
#반복문 한번 더 돌리기 -> 변수, 메모리낭비..


