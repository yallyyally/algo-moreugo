#k번째 수 찾기
#N개의 숫자로 이루어진 숫자열.
#해당 문자열 중 s~e를 오름차순 정렬했을 때 k번째로 나타는 숫자 출력

def KthNum():
    N,s,e,k=map(int,input().split())
    #배열 입력 받기
    numbers=list(map(int,input().split()))
    #s~e만 소팅
    numbers_filtered = numbers[s-1:e]
    #그냥 numbers에 바로 넣어주면 공간도 절약하고 좋음.
    numbers_filtered.sort()
    return numbers_filtered[k-1]


#테스트케이스 수
T = int(input())
# answers = [range(T)] -> range형 오브젝트 하나인 배열
# 한번에 테스트 케이스 별 답 출력하기 위함.
answers = [0 for i in range(T)]

for i in range(T):
    answers[i]=(KthNum())

for i in range(T):
    print("#",i+1,' ',answers[i])
    #바로바로 출력해줘도 되는거였음..
    #print("#%d %d" %(i+1, answers[i]))

