#k번째 큰 수
#N개의 자연수 카드가 있을 때,(중복 가능) 이중 3장의 합을 가능한 모든 경우의 수 다 기록할 경우
#중복제거 자료구조 ->""set""!!


N,K = map(int,input().split())
cards=list(map(int,input().split()))
sums=set()

for i in range(N):
    for j in range(i+1,N):
        for k in range(j+1,N):
            sums.add(cards[i]+cards[j]+cards[k])

#소팅하기 위해 리스트화
sums = list(sums)
sums.sort()
sums.reverse()
print(sums[K-1])

