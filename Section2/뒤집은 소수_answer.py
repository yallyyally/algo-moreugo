#뒤집은 소수
#자연수 N개 입력 ->뒤집은 후 소수이면 출력 (뒤집은 상태로)
#앞자리 0 무시
#def reverse(), def isPrime(x) 반드시 작성

def reverse(x):
    # 기본 매커니즘:
    # 1. 어떤 수 x가 있으면 (9010)
    # 2. t = x%10 (그 수의 1의자리 수)
    # 3. res = res*10 + t => 원래 있던 수 살을 붙이는 과정.
    # 4. x = x//10 (이렇게 가다가 0이 될 때까지)
    res = 0
    while x:
        t = x%10
        res = res*10 + t
        x//=10
    #시간은 문자열이 훨 빠름.
    return res

def isPrime(x):
    # ans=True
    # if x==1:
    #     ans=False
    # elif x==2:
    #     ans=True
    # else:
    #     for i in range(2,x):
    #         if x%i==0:
    #             ans=False
    #             break
    # return ans
    #######시간초과 에러 #####
    if x==1:
        return False
    #2~x-1 사이의 소수들이 체내다가 체내는 순간 out
    list = [1]*(x+1)
    for i in range(2,x):
        if list[i]: #소수면, 소수 아니면 (0이면 pass)
            j=2*i #이미 소수니까 그 배수부터 점검
            while j<=x:
                if j==x:
                    return False
                list[j] = 0
                j+=i

    return True
    #안체내지고 왔으면 True
def isPrime2(x): #
    if x==1:
        return False
    for i in range(2,x//2+1):
        #x//2가 x의 가능한 약수 중 제일 큰 수이므로 이 범위 안에서 나누면 된다.
        #체로 하면 약수의 다른 배수들까지 알아야하므로 번거롭,
        if x%i==0:
            return False
    else:
        return True #약수 못찾았음.

N = int(input())
numbers = list(map(int,input().split()))

for x in numbers:
    updown_x=reverse(x)

    if isPrime2(updown_x):
         print(updown_x,end=' ')
