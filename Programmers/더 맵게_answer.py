'''
파이썬 힙 라이브러리 설명

#힙을 import 하는 라이브러리
import heapq

#리스트L로부터 min heap 구성
#완전 이진 트리 -> 인덱스로 접근 가능.
heapq.heapify(L)

#min heap에서 최소값 삭제(반환) + 구조 유지
m = heapq.heappop(L) 

#minheap에 새로운 원소 x 삽입
heapq.heappush(L,x) 

'''
import heapq

def solution(scoville,K):
    answer = 0
    heapq.heapify(scoville)

    #한번 할 때마다 원소의 개수가 1 씩 줄어들고, 이때 종료하기 때문에 N-1번 실행한다.
    while True:
        #logN
        min1 = heapq.heappop(scoville)

        #중단 조건 1: 모든 음식의 스코빌 지수가 >=k
        if min1>=K:
            break
        #중단 조건 2: 힙의 크기가 줄어들다가 1이 되었는데도 <k
        elif len(scoville) ==0:
            answer = -1
            break
        
        #스코빌 지수를 조정해주어야 하고, 크기도 아직 하나 이상 남아있음.
        #logN
        min2 = heapq.heappop(scoville)
        
        new_scoville = min1 + 2*min2
        #logN
        heapq.heappush(scoville,new_scoville)
        answer += 1
##결론: NlogN ##
#만약 힙을 이용하지 않고 리스트로 비교해서 추가한다면, n^2이 될 것이다. 
    return answer