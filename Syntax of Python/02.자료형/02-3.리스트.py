#02. 파이썬 프로그래밍의 기초, 자료형
######################### 02-3. 리스트 #########################

import random as r
#1. 여러가지 리스트
a=[]
b=[1,2,3] #숫자만
c=['life','so','hard'] #문자열만
d=['life','s',5,'hard','100','%'] #문자열 숫자 둘다
e=['life','is',['so',555],['hard',299,'%'],'now!'] #리스트 속의 리스트

#2. 리스트의 인덱싱과 슬라이싱

##인덱싱(다중리스트 주의!)
print(e[2])#['so',555]
print(e[2][0])#'so'
print(e[2][0][0])#'s'

##슬라이싱
a=[1,2,3,4,5]
print(a[3:])#[4,5]
print(a[2:4])#[3,4] //[4]번째 포함X 주의

#3. 리스트 연산하기
##리스트 더하기(+)
a=[3,4,'Hello']
b=['not','Hell',77,9]
print(a+b)#[3,4,'Hello','not','Hell',77,9]

##리스트 반복하기(*)
print(a*2) #a*2=a+a=[3,4,'Hello',3,4,'Hello']

##리스트 길이구하기
print(len(a)) #3

###초보자가 범하기 쉬운 리스트 연산 오류
#print(a[1]+'hi')
#TypeError: unsupported operand type(s) for +: 'int' and 'str'
#자료형 에러
print(str(a[1])+"hi") #4hi

#4. 리스트의 수정과 삭제
del a[1]
print(a) #[3,4,'Hello'] -> [3,'Hello']
del a[0:]
print(a) #[]

#5. 리스트 관련 함수들
##리스트 요소 추가(append)
a.append([1,2,3,'hi'])###형식 주의!!, 한번에 하나씩만 추가 가능
print(a) #[[1,2,3,'hi']]
a.append(4)
print(a) #[[1,2,3,'hi'],4]

##리스트 정렬(sort)
del a[0:]
a=[5,4,6,8]
print(a.sort()) #암것도 반환 안함
print(a)
a.append('hi')
#a.sort() -> 자료형 다른 것끼리는 소팅 불가능
del a[0:]
a=['x','a','df']
a.sort()
print(a)#['a', 'df', 'x']

##리스트 뒤집기(reverse)
a.reverse()
print(a) #['x','df','a']

##위치 반환(index)
print(a.index('x')) #0
#print(a.index('dfd'))#Error

##리스트에 요소 삽입(insert)
#a.insert(1,'member') -> 1번 index에 member 문자열 추가
a.insert(4,3)
print(a) #['x','df','a',3] 사이 공백 무시
a.insert(0,5)
print(a) #[5,'x','df','a',3]

##리스트에 요소 제거(remove)
#a.remove(59) #Error
a.remove(5) ###인덱스 말고 원소 자체 제거
print(a) #['x','df','a',3]

##리스트에 요소 끄집어내기(pop)
print(a.pop()) #3
print(a) #['x','df','a']
###특정 인덱스 값만 pop 시킬 수 있음
#print(a.pop(2)) #'a'
#print(a)#['x','df']
##리스트에 포함된 요소 개수 세기(count)
a.append('x')
print(a.count('x')) #2
print(a.count('df'))#1
print(a.count('sdfdsf'))#0

##리스트 확장(extend)
###배열 형태로 넣어줘야함
a.extend([5,6,6])
print(a) #['x','df','a',5,6,6]
# a.extend(4,3,5) Error : extend() takes exactly one argument (3 given)

#list 활용 - 1 argument만 가능 -> 문자열 or 튜플 or rangeㄱㄴ
tmp = list((2,3,4,5))
print(tmp)
#[2, 3, 4, 5]

tmp = list('hellooo')
print(tmp)
#['h', 'e', 'l', 'l', 'o', 'o', 'o']

tmp = range(1,10)
print(list(tmp))
#[1, 2, 3, 4, 5, 6, 7, 8, 9]

#list+list만 가능, 문자열도 list로 바꿔줘야 함.
#print(list(tmp)+'456')
#TypeError: can only concatenate list (not "str") to list
print(list(tmp)+list('456'))
#[1, 2, 3, 4, 5, 6, 7, 8, 9, '4', '5', '6']

#합 구하기
tmp_list = list(tmp)
for i in tmp_list:
    if tmp_list.index(i) != len(tmp_list)-1:
        print(i,end=' + ')
    else:
        print(i,end=' = ')
print(sum(tmp_list))
#1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 = 45

#최대값 구하기
print(max(tmp_list)) #9
#최소값 구하기
print(min(tmp_list)) #1

print(min(1,3,5)) #1

#무작위로 섞기
tmp_list.sort() #반환형 None임에 유의.
print(tmp_list)
#[1, 2, 3, 4, 5, 6, 7, 8, 9]
r.shuffle(tmp_list)
print(tmp_list)
#[5, 9, 2, 3, 8, 6, 4, 7, 1]

#거꾸로 정렬
tmp_list.sort(reverse=True)
print(tmp_list)
#[9, 8, 7, 6, 5, 4, 3, 2, 1]

#리스트 초기화
tmp_list.clear()
#반환형 없음에 유의!
print(tmp_list)
#[]

#번외: range의 파라미터
range(10) #0~9
range(1,10) #1~9
range(0,100,2) #0->2->4->...->98

#문자열/리스트 출력
arr = [1,2,3,4,5]
for i in range(len(arr)):
    print(arr[i],end =' ')
    #1 2 3 4 5
print()

for x in arr:
    print(x, end =' ')
print()

sentence = 'abcdefg'
for i in range(len(sentence)):
    print(sentence[i],end=' ')
print()

for x in sentence:
    print(x,end=' ')
print()

#(인덱스 번호, 원솟값) <- 이 튜플형태로 출력하도록 하는 함수 enumerate
print(type(enumerate(sentence)))
#<class 'enumerate'> -> tuple로 이루어진 list라고 생각하면 쉬울 듯

for x in enumerate(sentence):
    print(x)
print()
'''
(0, 'a')
(1, 'b')
(2, 'c')
(3, 'd')
(4, 'e')
(5, 'f')
(6, 'g')
'''

#포매팅으로 구현
##for i,v in [(0,'a'),(1,'b'),...,(6,'g')] -> tuple을 포매팅.
for i,v in enumerate(sentence):
    print('index:{}, value:{}'.format(i,v))
print()
'''
index:0, value:a
index:1, value:b
index:2, value:c
index:3, value:d
index:4, value:e
index:5, value:f
index:6, value:g
'''