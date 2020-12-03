def solution(seat):
    answer = -1
    d = {}
    
    for s in seat:
        #list는 해쉬가 불가하므로 문자열로 만듦
        ##정수 -> str
        key = str(s[0]) + str(s[1])

        if d.get(key,0)==0: #자리 있음
            d[key] = 1
            answer+=1
    answer+=1

    return answer