#02. 파이썬 프로그래밍의 기초, 자료형
######################### 02-6. 집합 #########################

Jiphap=set([2,3,4])
print(Jiphap)
#{2, 3, 4}
##KEY만으로 이루어진 딕셔너리 같은 것?

#문자열 입력도 가능 -> 중복된 문자 제외해서 알아서 넣음
Jiphap=set('Hellowww')
print(Jiphap)
#{'l', 'e', 'w', 'H', 'o'}

#공집합
Gonjiphap= set()
print(Gonjiphap)
#set()

#집합의 특징: 중복x, 순서 없음(unordered)
#튜플,리스트와 다르게 인덱스 의미X, 인덱싱 불가
#print(Gonjiphap[0]) #TypeError: 'set' object does not support indexing
##tuple, list로 변하면 인덱싱 가능
list_Jiphap=list(Jiphap)
tuple_Jiphap=tuple(Jiphap)
print(list_Jiphap[0]) #l
print(tuple_Jiphap[1]) #e

#교집합, 합집합, 차집합 구하기
s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])

##1. 교집합
print(s1&s2)
print(s1.intersection(s2))
#{4,5,6}

##2.합집합
print(s1|s2)
print(s1.union(s2))
#{1,2,3,4,5,6,7,8,9}

##3.차집합
print(s1-s2)
print(s1.difference(s2))
#{1,2,3}
print(s2-s1)
print(s2.difference(s1))
#{8,9,7}

#집합 자료형 관련 함수들
#1.값 추가하기(add) -> 하나만 가능
s1.add(100)
print(s1)
#{1, 2, 3, 4, 5, 6, 100}

#2.값 여러 개 추가하기(update)
s1.update([200,300]) ##반드시 list로 한번에,,
print(s1)
#{1, 2, 3, 4, 5, 6, 100, 200, 300}

#3.특정 값 제거하기(remove_
s1.remove(1)
##하나만 가능!배열 형태 X
##TypeError: unhashable type: 'list'
print(s1)
#{2, 3, 4, 5, 6, 100, 200, 300}
