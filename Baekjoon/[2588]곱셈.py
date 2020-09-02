
#x의 10^n번째 자릿수 리턴
#463,2 ->60
def number(a,n):
    #385->85
    a = a%(10**n)
    #85->80
    a = a-a%(10**(n-1))
    return a

#input
x = int(input())
y = int(input())

numbers = [0]*3

for i in range(1,4):
    a = x*number(y,i)
    numbers.append(a)
    if a==1:
        print(a)
    else:
        print(a//(10**(i-1)))

print(sum(numbers))
