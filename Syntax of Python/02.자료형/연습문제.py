hongnumber = '881120-1068234'
index = hongnumber.index('-')
d= dict()

def q1():
    #홍길동씨의 평균 구하기
    kor=80
    eng=75
    mat=55
    total = kor+eng+mat
    #정수로 구하기
    print(total//3)
    #실수로 구하기
    print(total/3)

def q2():
    #자연수가 홀수인지 짝수인지 판별할 수 있는 방법
    args=13
    if args/2-args//2==0:
        print("짝수")
    else:
        print("홀수")

def q3():
    #주민등록번호 앞, 뒷부분 나누어 출력
    front=hongnumber[:index] #그 전까지
    back=hongnumber[index+1:] #그거 포함해서
    print('front:'+front)
    print('back:'+back)

def q4():
    print('홍씨 성별:'+hongnumber[index+1])

def q5():
    sentence='a:b:c:d'
    #a:b:c:d->a#b#c#d
    sentence_mod=sentence.replace(":","#")
    #반드시 저장해줘야댐
    print(sentence_mod)

def q6():
    list=[1,3,5,4,2]
    list.sort()
    list.reverse()
    print(list)

def q7():
    list=['Life','is','too','short']
    list=' '.join(list)
    print(list)

def q8():
    t =(1,2,3)
    t += (4,)
    print(t)

def q9():
    d['name']='python'
    d[('a',)] = 'python'
    #d[[1]]='python' -> TypeError: unhashable type: 'list'
    d[250]='python'

def q10():
    d = {'A':90, 'B':80, 'C':70}
    print(d.pop('B'))
    print(d) #pop 시킨거 사라짐
    print(d.pop('z',0))#디폴트값 반환

def q11():
    s = set([1,1,1,2,2,3,3,3,4,4,5])
    print(s)

def q12():
    a=b=[1,2,3]
    a[1]=4
    print(b) #1,4,3

#q1()
#q2()
#q3()
#q4()
#q5()
#q6()
#q7()
#q8()
#q9()
#q10()
#q11()
#q12()