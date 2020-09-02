
def findDiff(num):
    return num%10 - num//10%10

def isitSuyeol(num):
    diff = findDiff(num)
    num //= 10

    while num>9:
        if findDiff(num) != diff:
            return False
        num//=10
    return True

N = int(input())


if N<100:
    print(N)

else:
    cnt = 99
    i=100
    while i<=N:
        if isitSuyeol(i):
            cnt+=1
            i+=11
        else:
            i+=1

    print(cnt)