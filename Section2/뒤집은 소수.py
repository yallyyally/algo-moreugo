#뒤집은 소수
#자연수 N개 입력 ->뒤집은 후 소수이면 출력 (뒤집은 상태로)
#앞자리 0 무시
#def reverse(), def isPrime(x) 반드시 작성

def reverse(x):
    #x를 거꾸로 뒤집어 줌
    x=list(x)
    x.reverse()
    res=''
    for y in x:
        res+=y

    return int(res)

def isPrime(x):
    ans=True
    if x==1:
        ans=False
    elif x==2:
        ans=True
    else:
        for i in range(2,x):
            if x%i==0:
                ans=False
                break
    return ans

N = int(input())
numbers = list(input().split())

for x in numbers:
    updown_x=reverse(x)

    if isPrime(updown_x):
         print(updown_x,end=' ')
