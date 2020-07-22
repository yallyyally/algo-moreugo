#02. 파이썬 프로그래밍의 기초, 자료형
######################### 02-8. 자료형에값저장 #########################
from copy import copy

#1.리스트 복사
a=[1,2,3]
##주소값 복사
b=a
##내용만 복사
c=a[:]
##copy모듈로 내용만 복사
d=copy(a)
a[1]=5
print(b)
#[1, 5, 3]
print(c)
print(d)
#[1, 2, 3]

#2. 변수 만들기
##튜플로 만들기
a,b = ('phtyhon','life')
(a,b) ='python','life'
#값 바꾸기
a,b = b,a
print(a)
##리스트로 만들기
[a,b]=['python','life']
a,b=b,a
print(a)

#값 지정하기
a,b,c=1,2,3
print (a,b,c)
#3 2 1
a,b,c = c,a,b
print(a,b,c)
#3 1 2
print (a,b,c, sep = ' * ')
#3 * 1 * 2
print (a,b,c, sep ='\n')
print (a, end = ' end')
#3 end