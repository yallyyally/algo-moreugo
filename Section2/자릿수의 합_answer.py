#자릿수의 합
#자연수 N개 입력 -> 각 자릿수의 합.
#그 자릿수의 합이 최대인 자연수 출력
#자릿수 합 구하는 함수 digit_sum(x) 사용

def digit_sum(x):
    sum=0
    #수 -> 문장으로 바꿔서 처리!
    for i in str(x):
        sum+=int(i)
    return sum

N = int(input( ))

#N개의 자연수 입력받아서 배열에 넣기
numbers = list(map(int,input().split()))

max=-2147000000

for x in numbers:
    tot = digit_sum(x)
    if tot>max:
        max=tot
        res=x
        #index 대신 직접 답을 저장해주는 변수하나를 지정해서 시간 단축.

print(res)