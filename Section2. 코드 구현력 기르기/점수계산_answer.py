#점수 계산
#OX퀴즈에서 연속적으로 맞힐 경우 가산점.
#+1....+K, 틀리면 0점, 맞으면 또 +..
#문제수(N)과 채점 결과 제공 (맞으면 1,틀리면 0)

N = int(input())
results=list(map(int,(input().split())))

score=0
series=0 #연속 몇갠지
#기본 알고리즘은 똑같음 헤
for x in results:
    #맞음
    if x:
        series +=1
        score += series

    #틀리면 연속 사라짐..
    else:
        series=0

print(score)