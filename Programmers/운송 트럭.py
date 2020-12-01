def solution(max_weight, specs, names):
    answer = 1  
    weight_loading = 0
    #spec ����
    spec = {}
    for s in specs:
        spec[s[0]] = int(s[1])
    for food in names:
        weight_food = spec[food]
        #���ϱ�
        if weight_loading + weight_food>max_weight:
            #���� �ʰ�
            answer+=1
            weight_loading = weight_food
        else:
            #���� ����
            weight_loading+=weight_food
            
    return answer