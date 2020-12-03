def solution(N, number):
    answer = 0
    #각 연산 횟수 당 중복대는 값 제외하고 저장하기 위함
    s = [set() for x in range(8))]
    #최솟값이 8보다 크면 (8번 해도 안나오면) -1 리턴하니까 8만 필요
    
    for i, x in enumerate(s, start = 1):#i는 1부터 시작(시작 인덱스 지정)
        #사칙연산 말고 그냥 덧붙여서 발s생하는 것들 미리 적어놓기
        x.add(int(str(N)*i))

    #사칙연산 계산
    #i: 연산 사용 횟수 이므로 7 만큼 순환.
    for i in range(8):# 연산 횟수 0회부터 시작
        #연산 사용 횟수.(숫자 개수 - 1)
        for j in range(i): 
            for op1 in s[j]:
                for op2 in s[i-j-1]: #연산 횟수 지금 추가될 것임
                    s[i].add(op1+op2)
                    s[i].add( op1 - op2 )
                    s[i].add(op1 * op2)
                    if op2!=0:
                        s[i].add(op1 // op2)
        #i번 연산 해서 구할 수 있는 경우의 수 다 구함
        if number in s[i]:
            answer = i+1
            break
    #다 구했는데 없음
    else:
        answer = -1



    return answer