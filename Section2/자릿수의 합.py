#자릿수의 합
#자연수 N개 입력 -> 각 자릿수의 합.
#그 자릿수의 합이 최대인 자연수 출력
#자릿수 합 구하는 함수 digit_sum(x) 사용

def digit_sum(x):
    sum=0
    #x가 0이 될때까지 반복
    while(x):
        sum+=x%10
        x //=10
    return sum

N = int(input())

#N개의 자연수 입력받아서 배열에 넣기
numbers = list(map(int,input().split()))

max=digit_sum(numbers[0])
maxIndex=0
for i in range(1,N):
    if digit_sum(numbers[i])>max:
        max=digit_sum(numbers[i])
        maxIndex=i

print(numbers[maxIndex])