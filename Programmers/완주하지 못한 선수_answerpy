def solution(participant, completion):
    answer = ''

    d = {}
    #N시간
    for x in participant:
        #참가자 
        d[x] = d.get(x,0)+1 #없으면 0
    #N시간
    for x in completion:
        d[x]-=1

    #d.items -> (key,value) tuple list in dictionary
    #N시간
    dnf = [k for k, v in d.items() if v>0] 
    #value가 0보다 큰 값의 key들
    #value, split 처럼 여러개 자료가 나오고, 이걸 한번에 리스트로 묶음
    answer = dnf[0]

    #시간복잡도: 
    return answer