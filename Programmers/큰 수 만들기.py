# -*- coding:utf-8 -*-
def solution(number, k):
    answer = ''
    pocket = [] #선택된 숫자들 넣음
    
    for i in range(len(number)):  #넣으려면 있는 것보다 커야 함. k만큼만 빼기.
        #pocket에 넣을지 말지 선택.
        #없는거면 검사해줄 필요 없이 그냥 넣음 
        #k개 내에서 나보다 작은 것들을 밀어내는 과정
        while len(pocket)>0 and k>0:
            if pocket[-1]<number[i]:
                pocket.pop(-1)
                k-=1
            else:
                break
 #종료 - pocket의 크기가 0, k==0, 다 밀어냄
        #k가 0이면 남은거 다 넣기, 종료
        if k==0:
            pocket.append(number[i:])
            break
        ##pocket이 0이거나, 다 밀어  냈으면 일단 넣고 보기        pocket.append(number[i])
    #k아직 덜 채움 -> 뒤에서 k개 만큼자르기
    if k>0:
        pocket = pocket[:-k]
    answer = ''.join(pocket) #리스트 -> 문자열 만들때
    print(answer)
    return answer

number = "1924"
k=2
solution(number,k)