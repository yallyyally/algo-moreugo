def solution(numbers):
    #N
    numbers = [str(x) for x in numbers]
    #NlogN
    numbers.sort(key = lambda x: (x*4)[:4], reverse=True)
    #####코너 케이스#####
    if numbers[0]=='0':
        answer=='0'
    else:
        #N
        answer = ''.join(numbers)
    return answer
    ###전체 복잡도 NlogN