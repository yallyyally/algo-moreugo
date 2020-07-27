def add(a,b):
    c=a+b
    #print(c)
    return c

def add2(a,b):
    c=a+b
    d=a-b
    return c,d #tuple 형태로 리턴.

#소수면 true, 소수가 아니면 false
def isPrime(x):
    for i in range(2,x): #2 ~ x-1
        if x%i==0:
            return False
    return True

#함수는 항상 mainscript 위에 있어야.....define 되있단거 알아야 됨

# add(3,2)
print(add(3,2)) #5
print(add2(4,8)) #(12,-4)

print(isPrime(13)) #True
print(isPrime(14)) #False

a = [12,13,7,9,19]
for y in a:
    if isPrime(y):
        #소수면 출력
        print(y,end=' ')
#13 7 19


