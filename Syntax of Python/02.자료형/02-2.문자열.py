#02. 파이썬 프로그래밍의 기초, 자료형
#########################02-2문자열 자료형#########################

#큰 따옴표, 작은 따옴표, 큰따옴표3개, 작은 따옴표 3개
sent1 = "Hello"
sent2='World'
sent3="""!!!"""
sent4='''hi~'''

#문자열 더하기
print(sent1+sent2+sent3+sent4) #HelloWorld!!!hi~

#문자열 길이
print(len(sent1))#5

#문자열 인덱싱
a = "Hello world!"
print(a[-1]) #!
print(a[-8]) #o

#문자열 슬라이싱
b = a[1]+a[3]+a[-3]
print(b)#ell
print(a[0:4]) #Hell ,0~3까지 프린트, 0<=a<3
print(a[:2])#He
print(a[5:])# world!

#문자열 포매팅 - %만 사용, format(인덱스, 숫자), f(변수명만)
##1. % 사용
print('I got %.2f in this semester' %4.3) #I got 4.30 in this semester
print('what did %s say?'%'you') #what did you say?
print( 'I got %d presents for my %s' %(4,"birthday"))#I got 4 presents for my birthday
##2.format 함수 사용하여 문자열 포매팅
###숫자 그대로 넣기
print('I ate {0} apples for {1} days.'.format(1,3)) #I ate 1 apples for 3 days.
###숫자와 문자 인덱스로 넣기
print('I ate {0} apples for {1}days.'.format(5,'holi'))#I ate 5 apples for holidays.'
###숫자와 문자 이름으로 넣기
print('I ate {number} apples for {days} days.'.format(number=5,days='rest'))
print('I ate %d apples for %s days.'%(5,'rest'))
#I ate 5 apples for rest days.
####인덱스와 이름 혼용
print('I ate {0} apples for {days} days'.format(5,days='rest'))#I ate 5 apples for seven days

#소수점 표현하기
y=3.1415926
print('원주율: {0:0.4f} {1:0.2f}'.format(y,y))
print('원주율: {first:0.4f} {second: 0.2f}'.format(first=y,second=y))
print('원주율: %.4f %.2f'%(y,y))
print(f'원주율: {y:0.4f} {y:0.2f}')
#원주율: 3.1416 3.14

##3. f 사용하여 문자열 포매팅 - 옆에 format함수나 %()없어도 바로바로 변수 출력 가능
name='신준희'
age=23.4
print(f'나의 이름은 {name}이며 나이는 {age-5}임니다.')
print('나의 이름은 %s이며 나이는 %.1f입니다.'%(name,age-5))
print('나의 이름은 {0}이며 나이는 {second:0.1f}입니다.'.format(name,second=age-5))
#나의 이름은 신준희이며 나이는 18.4입니다.
#딕셔너리에서 f 사용하기
d={'name':'탕볶밥','price':6000}
print(f'나의 이름은 {d["name"]}입니다. 가격은 {d["price"]}입니다.')
##속성 무족건 큰따옴표 써야댐
#나의 이름은 탕볶밥입니다. 가격은 6000입니다.


#왼쪽, 가운데, 오른쪽 정렬
hello='Hello!'

#왼쪽 정렬
print('%-10s'%hello)
##인덱스
print('{0:<10}'.format(hello))
##이름
print('{hello:<10}'.format(hello=hello))
print(f'{hello:<10}')

#오른쪽정렬
print('%10s'%hello)
print('{0:>10}'.format(hello))
print('{hellow:>10}'.format(hellow=hello))
print(f'{hello:>10}')
#가운데 정렬
print('{0:^10}'.format('Hello!'))
print('{hello:^10}'.format(hello='Hello!'))
print(f'{hello:^10}')
#공백채우기 (가운데 정렬)
print('{0:~^10}'.format(hello))
print('{greeting:~^10}'.format(greeting=hello))
print(f'{hello:~^10}')
#공백채우기2 (오른쪽 정렬)
print('{0:~>10}'.format('hello!'))
print('{greeting:~>10}'.format(greeting=hello))
print(f'{hello:~>10}')
#Hello!
#    Hello!
#  Hello!
#~~hello!~~
#~~~~hello!

