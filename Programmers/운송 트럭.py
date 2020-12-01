def solution(max_weight, specs, names):
    answer = 1  
    weight_loading = 0
    #spec 정리
    spec = {}
    for s in specs:
        spec[s[0]] = int(s[1])
    for food in names:
        weight_food = spec[food]
        #더하기
        if weight_loading + weight_food>max_weight:
            #무게 초과
            answer+=1
            weight_loading = weight_food
        else:
            #무게 안전
            weight_loading+=weight_food
            
    return answer