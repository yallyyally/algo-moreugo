N,M = map(int,input().split())
cards = list(map(int,input().split()))

cards.sort(reverse=True)
sum = 0
max = 0
for i in range(N):
    sum = cards[i]
    if sum>=M:
        continue
    for j in range(i+1,N):
        sum+=cards[j]
        #미리 처리
        if sum>=M:
            sum-=cards[j]
            continue
        for k in range(j+1,N):
            if sum+cards[k]<=M and max<sum+cards[k]:
                max = sum+cards[k]
        else:
            sum-=cards[j]
    else:
        sum-=cards[i]

print(max)