#-*- coding: utf-8 -*-
def solution(numbers):
    answer = ''
    numbers_new = [None]*len(numbers)
    #1. 다 문자열 형태로 바꿔주기
    for i in range(len(numbers)):
        numbers_new[i] = [str(numbers[i]), i] #본래 인덱스도 같이 저장
        
    #2.다 네자릿수로 바꿈 - 자리가 모자라면 끝 숫자를 연장하는 방식
    for i in range(len(numbers)):
        for j in range(4-len(numbers_new[i][0])):
            numbers_new[i][0]+=numbers_new[i][0][len(numbers_new[i][0])-1]
    #네개의 키로 소팅
    numbers_new.sort(key = lambda x:(int(x[0][0]), int(x[0][1]), int(x[0][2]), int(x[0][3])), reverse = True)
    for n in numbers_new:
        answer+=str(numbers[n[1]])
    return answer

numbers = [3, 30, 34, 5, 9]
print(solution(numbers))