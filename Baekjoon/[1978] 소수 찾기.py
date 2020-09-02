import math

def primeNumber(x):
    if x==1:
        return False

    limit = math.floor(math.sqrt(x))
    for i in range(2,limit+1): #2에서부터 약수가 하나라도 있으면 소수 아님
        if x%i==0:
            return False
    return True


N = int(input())
numbers = list(map(int,input().split()))

cnt=0
for x in numbers:
    if primeNumber(x):
        cnt+=1
print(cnt)