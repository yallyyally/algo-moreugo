def solution(numbers):
    answer = ''
    
    for i in range(len(numbers)):
        numbers[i] = str(numbers[i])
    numbers.sort(key = lambda x :( x[0],x[1%len(x)],x[2%len(x)],x[3%len(x)]),reverse = True)
      #가장 큰 '수' -> '0','0','0','0', -> '0000'도 0으로
    if numbers[0]=='0': #가장 큰 수가 0 -> 오직 원소 하나 "00000"
        answer = '0'
    else:
        for n in numbers:
            answer +=n
    
    return answer