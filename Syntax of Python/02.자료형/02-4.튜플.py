#02. 파이썬 프로그래밍의 기초, 자료형
######################### 02-4. 튜플 #########################
#튜플은 리스트와 비슷하지만, 값의 삭제와 수정이 불가능하며 ( )로 둘러싼다

t1=()
t2=(1,) #요소가 하나일땐 반드시 콤마
t3=(1,2,3)
t4=(1,5,'gh0') #다른 자료형도 ㅇㅋ
t5=('ㅁ','b',(5,'f')) #튜플 속의 튜플

#del t1[0] //삭제 불가-TypeError: 'tuple' object doesn't support item deletion
#t1[0]='c' //수정 불가-TypeError: 'tuple' object does not support item assignment
#t3[1]='v' //추가 불가-TypeError: 'tuple' object does not support item assignment

#1. 인덱싱하기
print(t4[2]) #'gh0
#2. 슬라이싱하기
print(t4[:-2])#(1,)
#3. 더하기
print(t3+t4) #(1,2,3,1,5,'gh0')
#4. 곱하기
print(t3*2) #(1,2,3,1,2,3)
#5. 길이 구하기
print(len(t5)) #3