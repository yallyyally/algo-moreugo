import math

def solution(brown, red):
    answer = []
    #red의 공약수 중 큰것 - 가로, 작은 것 - 세로.
    
    for sero in range(1,math.floor(math.sqrt(red))+1):
        if red % sero ==0:
            #약수가 맞는 경우
            garo = int( red/sero)
            if 4+2*(garo+sero)==brown:
                answer.append(garo+2)
                answer.append(sero+2)
    return answer