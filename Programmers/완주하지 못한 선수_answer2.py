def solution(participant, completion):
    #문자열 정렬을 사용한 풀이법

    #NlogN
    participant.sort()
    #NlogN
    completion.sort()

    #N
    for i in range(len(completion)): #len(completion)<len(participant), index out of range 에러 방지
        if participant[i]!=completion[i]:
            return participant[i]
    
    return participant[len(participant)-1]