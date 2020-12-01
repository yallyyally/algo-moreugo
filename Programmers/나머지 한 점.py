def solution(v):
    answer = []
    garo = {}
    sero = {}
    
    for x in v:
        if x[0] not in garo:
            garo[x[0]] = 1
        else:
            garo[x[0]]+=1
        if x[1] not in sero:
            sero[x[1]] = 1
        else:
            sero[x[1]]+=1
    
    for g in garo:
        if garo[g]<2:
            answer.append(g)
    for s in sero:
        if sero[s]<2:
            answer.append(s)
            
    
    return answer