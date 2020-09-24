import sys

#sys.stdin = open("in3.txt","rt")

N,k = map(int,sys.stdin.readline().split())

#N개의 랜선 k개로 균등하게 만들기
cables = []
for _ in range(N):
    cables.append(int(sys.stdin.readline()))
cables.sort(reverse = True)
#해싱 테이블
#개수 - 최대 길이
count = {}
dividedCount = []
#각 랜선을 몇개로 나눌 지 저장.

dividedCount.append(2)
#제일 큰건 2로 나누면서 시작

for _ in range(N-1):
    dividedCount.append(1)
#두번째 ~젤 작은건 그 크기 자체로 나누면서 시작.

breakflag = [0]*N #이게 N개가 되면 break
turn = 0 #나눌 기준이 될 케이블 번호
breakcnt =0
while(True):
    #N개로 나눴을 때 다 cnt를 초과하면 break
    if breakflag[turn]==0:
        cnt=0
        equalLength = cables[turn]//dividedCount[turn] #나눌 기준이 될 길이.
        #그 길이 자체로 나눌때
        for i in range(N):
            cnt += cables[i]//equalLength

        if cnt==k:
            breakflag[turn] = 1
            breakcnt+=1
            if count.get(k) is None or count[k] < equalLength:
                count[k] = equalLength
            if breakcnt>=N:
                break

        elif cnt>k:
            breakflag[turn] =1
            breakcnt+=1
            if count.get(cnt) is None or count[cnt] < equalLength:
                count[cnt] = equalLength
            if breakcnt>=N:
                break
        else:
            dividedCount[turn]+=1
    #print('equal',equalLength)
    turn = (turn+1)%N

while count.get(k) is None:
    k+=1

print(count[k])