#주사위 게임
#N명이 주사위를 던질 때, (1~6) 가장 많은 상금을 받은 사람
#다 같은 수 ->1X,000원
#두개만 같은 수->1,X00원
#다 다른 수 -> X00원

max=0
#어차피 주사위 개수 세개로 정해져 있는 거니까 배열 쓸 필요 X ㅠㅠ
N = int(input())

for i in range(N):
    tmp = input().split()
    #오름차순 정렬.
    tmp.sort()
    a,b,c = map(int,tmp)
    #3 3 5 이렇게 정렬된 상태의 abc

    #3개 다 같을 때
    if a==b and b==c:
        prize = 10000+a*1000
    #앞에 2개
    elif a==b: #b랑 c가 같은 경우도 있지만 눈 계산도 해야하니까..
        prize = 1000+a*100
    #뒤에 2개
    elif b==c:
        prize = 1000+b*100
    #다다름 -> 이럴려고 정렬한거.
    else:
        prize=c*100

    if prize>max:
        max=prize



#최대 상금 출력
print(max)
