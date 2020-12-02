import math

def solution(progresses, speeds):
    days = 0
    answer = []
    for p in range(len(progresses)):
        progresses[p]+=speeds[p]*days
        if progresses[p]<100:
            #days 추가
            days+=math.ceil((100-progresses[p])/speeds[p])
            answer.append(1)
        else:
            answer[len(answer)-1]+=1
        
    return answer