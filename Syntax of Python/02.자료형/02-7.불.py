#02. 파이썬 프로그래밍의 기초, 자료형
######################### 02-7. 불 #########################

a =True
b = False

print(type(a))
print(type(b))
#<class 'bool'>
a = [1,2,3,4]
while a:
    print(a.pop())
print(a)
b=0
print(bool(b)) #False
a=3
print(bool(a)) #True