#대표값
#수학성적 평균과 가장 가까운 학생 번호 구하기
#답이 두개 ->높은 학생
#답이 여러개 -> 번호가 빠른 학생

N = int(input())
scores = list(map(int,input().split()))
min=2147000000 #정수 최대값
#평균구하기
# for i in scores:
#     avg += i

#sum 메소드 잊지 말자..!! + 변수도,,
avg = round(sum(scores)/N)

#enumerate 잊지 말자,,->(인덱스, 값) 튜플형태로 출력하도록 함.
for number,score in enumerate(scores):
    diff= abs(avg-score)
    #작을 때
    if diff<min:
        min=diff
        score_nearavg=score
        #번호, 점수,차이 저장
        ans=number+1
    #같을 때
    elif diff==min:
        #점수가 큰 학생걸로. -> 점수가 같으면 자동으로 앞에 학생 적용
        if score>score_nearavg:
            score_nearavg=score
            ans=number+1
        #굳이 두번 정렬할 필요 없도록..

print(avg,ans)
