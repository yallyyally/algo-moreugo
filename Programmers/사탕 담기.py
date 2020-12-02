answer = 0
def find(min,weights,m):
    global answer
    if m==0:
        answer+=1
    elif m>0:
        #min 이후의 값 삽입해서 알아보란 뜻
        for i in range(min+1,len(weights)):
            find(i,weights,m-weights[i])
    #그 외는 초과했으므로 호출 x

def solution(m, weights):
    global answer
    for i in range(len(weights)):
        find(i,weights,m-weights[i])
    return answer