#02. 파이썬 프로그래밍의 기초, 자료형
#########################02-9 변수 입력#########################

a = input("숫자를 입력하세요: ")
print(a)

a,b = input("숫자 2개를 입력하세요").split()
#a,b = map(int,input("숫자 입력").split())
#map(원하는 자료형, 자료 값) = 입력할 변수
#공백 기준으로 구분
print(type(a)) #class 'str'
a= int(a)
b = int(b)
print(type(a)) #class 'int'
print (a+b)