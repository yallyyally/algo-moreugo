import math
#숫자만 추출
#문자열 ->숫자만 추출해서 자연수 만들기 + 약수 개수 출력

#문자열 -> 숫자만 추출해서 자연수 만들기
def strToInt(sentence):
    sentence = list(sentence)
    numbers=[]
    for x in sentence:
        if x.isdigit():
            numbers.append(x)
    #['0','2','8']
    sentence = ''
    for x in numbers:
        sentence+=x
    sentence = int(sentence)
    return sentence
#정수 -> 약수 개수
def countYaksu(number):
    cnt=0
    sqrt = math.sqrt(number)
    sqrt = math.floor(sqrt)

    for x in range(1, sqrt):
        if number%x==0:
            cnt+=2
    if number%sqrt==0:
        if number/sqrt==sqrt:
            cnt+=1
        else:
            cnt+=2
    return cnt

sentence = input()
number = strToInt(sentence)
print(number)
print(countYaksu(number))