def solution(N, number):
    answer = 0
    
    val = [set() for x in range(8)]
    
    #N 붙이는 연산으로 일단 초기화.
    #i는 연산 횟수 == N사용횟수 -1
    for i in range(8):
        val[i].add(int(str(N)*(i+1)))
    
    #사칙연산 수행하면서 number 찾기 (찾으면 바로 break) 
    for i in range(len(val)):
        #i번 연산으로 얻을 수 있는 값들의 집합의 원소를 추가하기.
        for j in range(i): #j번 연산 + 사칙 연산 + (i-j-1)번 연산 = i번 연산
                             #이 연산에서 피 연산자를 찾는다.
            for op1 in val[j]:
                for op2 in val[i-j-1]:
                    val[i].add(op1 + op2)
                    val[i].add(op1 - op2)
                    val[i].add(op1 * op2)
                    if op2 != 0:
                        val[i].add(op1 // op2)
        if number in val[i]:
            answer = i+1
            break
    else:
        answer = -1
        
    return answer
    