#02. 파이썬 프로그래밍의 기초, 자료형
######################### 02-5. 딕셔너리 #########################
#Hash와 비슷
#key와 value를 한 쌍으로 가짐
#리스트, 튜플과 달리 순차적으로 구하지 않고 key를 통해 value를 얻는다.
#key로는 변하지 않는 값, value로는 변하든 변치않든 상관x
#{key1:value1, key2:value2,...}

dic ={'name':'joonhey','phone':242.40210,1:[2,3,4]}
#문자열 말고도 정수, 실수, 리스트 등 다양한 자료형이 key와 value 로 올 수 있다.

#1. 딕셔너리 쌍 추가, 수정,삭제하기
dic['addedKey'] = 'addedVal'
dic['name']='gildong'
print(dic)
#{'name': 'gildong', 'phone': 242.4021, 1: [2, 3, 4], 'addedKey': 'addedVal'}

del dic[1] #del[Key]
print(dic)
#{'name': 'gildong', 'phone': 242.4021, 'addedKey': 'addedVal'}

#2. 딕셔너리를 사용하는 방법
#딕셔너리에선 dic[인덱스]가 아니라 dic[Keyname]이다.
dic[3.14]='pi'
print(dic[3.14])#pi
##주의사항1: 같은 key 가 두 개 이상일 경우 앞 key-value쌍은 무시된다.
dict={1:'one',1:'하나'}
print(dict[1]) #하나
##주의사항2: key에 list는 불가능, tuple은 가능!

#3. 딕셔너리 관련 함수들
##(1)Key만 보고싶을 때.
print(dic.keys())
#2.7버전까지는 리스트를 돌려줬지만 메모리 낭비가 발생하므로 dict_keys 객체로 돌려줌
#dict_keys(['name', 'phone', 'addedKey', 3.14])
print(list(dic.keys())) #굳이 객체 -> 리스트로 만드는 법
#['name', 'phone', 'addedKey', 3.14]
#dict_keys 객체 사용법,, append,insert,pop,remove,sort는 불가

for key in dic.keys():
    print(key)
#name
#phone
#addedKey
#3.14

##(2)Value만 보고 싶을때
print(dic.values())
#dict_values(['gildong', 242.4021, 'addedVal', 'pi'])
print(list(dic.values()))
#['gildong', 242.4021, 'addedVal', 'pi']

##(3)Key,Value가 묶인 tuple로 보고 싶을 때
print(dic.items())
#dict_items([('name','gildong'),('phone', 242.4021), ('addedVal', 'pi')])
print(list(dic.items()))
#[('name', 'gildong'), ('phone', 242.4021), ('addedKey', 'addedVal'), (3.14, 'pi')]

##(4) 딕셔너리 초기화
dic.clear()
print(dic)
#{}

##(5)KEY 이용해서 VALUE 보기 (get)
print(dict[1])
print(dict.get(1))

###둘의 차이점: 존재하지 않는 key값을 이용할 때
#print(dict[2.4]) #에러
print(dict.get(2.4)) #None

###key 가 있는지 없는지 확실하지 않을 때 디폴트 값 사용하기
print(dict.get(2.4,'default')) #default

##(6)해당 Key가 딕셔너리에 존재하는지 조사 (in)
print('name' in dict) #False
print(1 in dict) #True