#03. 프로그램의 구조를 쌓는다!제어문
######################### 03-3. 반복문 연습문제 #########################

#1. 1부터 N까지 홀수 출력하기
#N = map(int,input())
#map 자체가 변수 여러개로 묶인 객체이므로 변수가 하나일땐 쓰면 안됨
N = int(input("N 입력:"))

for i in range(1,N+1):
    if i%2:
        print(i)
print('=================')

#2. 1부터 N까지의 합 구하기
sum=0
for i in range(1,N+1):
    sum +=i
print("합:",end='')
print(sum)
print('=================')

#3. N의 약수 출력하기
for i in range(1,N-1):
    if N%i==0:
        print(i, end=' ')