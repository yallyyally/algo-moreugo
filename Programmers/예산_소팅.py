def solution(d, budget):
    answer = 0
    money = 0
    d.sort()
    for dept in range(len(d)):
        if money + d[dept] <=budget:
            money+=d[dept]
            answer+=1
    return answer