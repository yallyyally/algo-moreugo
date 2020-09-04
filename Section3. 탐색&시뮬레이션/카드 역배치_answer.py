
#swap 하는 법: a,b = b,a

a = list(range(21)) #0부터 20까지 생김...

for _ in range(10):
    s,e = map(int,input().split())
    #(e-s+1) 회동안 돈다,,!
    #reverse 함수 그대로 쓰는 것보다 최대 7배 시간 절약.
    for i in range((e-s+1)//2):
        a[s+i],a[e-i] = a[e-i],a[s+i]
a.pop(0) #맨 앞꺼 꺼내기
for x in a:
    print(x,end = ' ')
