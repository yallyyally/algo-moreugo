#주사위 게임
#N명이 주사위를 던질 때, (1~6) 가장 많은 상금을 받은 사람
#다 같은 수 ->1X,000원
#두개만 같은 수->1,X00원
#다 다른 수 -> X00원

max=-2147000000
dice = [0]*6
N = int(input())

for i in range(N):
    a,b,c=map(int,input().split())
    dice[a-1]+=1
    dice[b-1]+=1
    dice[c-1]+=1
    #금액 계산
    ##다 똑같
    if dice[a-1]==3:
        prize=10000+a*1000
    else:
        ##두개만 똑같
        ###그게 a
        if dice[a-1]==2:
            prize=1000+a*100
        ###a 빼고 똑같
        elif dice[b-1]==2:
            prize=1000+b*100
        ###다다름
        else:
            #a,b,c중 제일 큰게 머임?
            for j in range(5,0,-1):
                if(dice[j]!=0):
                    prize=(j+1)*100
                    break
    dice[a-1]=0
    dice[b-1]=0
    dice[c-1]=0

    #최대상금
    if prize>max:
        max=prize



#최대 상금 출력
print(max)
