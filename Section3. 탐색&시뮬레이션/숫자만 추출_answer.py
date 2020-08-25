#숫자만 추출
#문자열 ->숫자만 추출해서 자연수 만들기 + 약수 개수 출력

#문자열 -> 숫자만 추출해서 자연수 만들기
def strToInt(sentence):
    res = 0
    for x in sentence:
        if x.isdecimal(): #isdigit은 2^3도 다 숫자로 처리.
            res=res*10+int(x)
            #문자섞인 문자열을 정수로 만드는 방법,
            #첫자리의 0도 계속 무시됨
    print(res)
    return res
#정수 -> 약수 개수
def countYaksu(number):
    cnt=0
    for i in range(1,number+1):
        if number%i==0:
            cnt+=1
    print(cnt)

sentence = input()
countYaksu(strToInt(sentence))
