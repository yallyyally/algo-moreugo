# 람다함수 -> 일종의 표현식이라고도 함.

def plus_one(x):
    return x+1

#plus_one 함수를 람다함수로 표현
plus_one_lamda= lambda x:x+2

print(plus_one(2)) #3
print(plus_one_lamda(3)) #5

#유용할 때 : 내장함수의 인자로 사용될 경우
#map: (함수명, 자료) -> 자료는 iterable한 객체 (리스트, 튜플)만 가능
a=[1,2,3]
b=(1,2,3)
print(list(map(plus_one,a)))
print(list(map(lambda x:x+1,a)))
print(map(plus_one,b))

#[2,3,4]
#list화 안하면 -><map object at 0x0000027D45872DD8>

