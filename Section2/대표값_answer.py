#대표값
#수학성적 평균과 가장 가까운 학생 번호 구하기
#답이 두개 ->높은 학생
#답이 여러개 -> 번호가 빠른 학생

N = int(input())
scores = list(map(int,input().split()))
avg=0

#평균구하기
for i in scores:
    avg += i

avg = round(avg/len(scores),0)

#round(p,q) : p를 q까지 반올림
# math.ceil(i) : 올림
# math.floor(i) : 내림
# math.trunc(i) : 버림

#평균과 가까운 학생
#numbers list 만듦 -> 소팅.
# 다 돌렸을때 크기가 1이면 그 점수
# 크기가 2이상인데 다 같은거 ->번호 빠름
#크기가 2 이상인데 다름 -> 큰거(>번호빠른거)
diff= abs(avg-scores[0])
#(번호,점수) tuple로 이루어진 list
near_avg=[(1,scores[0])]

for i in range(1,len(scores)):
    #같은 경우 list에 추가
    if abs(avg-scores[i])==diff:
        near_avg.append((i+1,scores[i]))
    #더 작은 경우 list 초기화 후 추가
    elif abs(avg-scores[i])<diff:
        near_avg.clear()
        near_avg.append((i+1,scores[i]))
        diff=abs(avg-scores[i])

print("%d"%avg,end=' ')
#점수가 다 같으면 빠른 번호
if near_avg[0][1]==near_avg[len(near_avg)-1][1]:
    print(near_avg[0][0])
else: #번호 먼저
    near_avg=sorted(near_avg,key=lambda x:x[0])
    #성적 그 다음(우선순위 높음)
    near_avg.sort(reverse=True,key=lambda x:x[1])
    #2차원 배열
    print(near_avg[0][0])
