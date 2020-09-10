path = []
N = 0
global cnt

 #from -> to 로 n번째 원판을 이동시킴
def hanoi(f,m,t,n):
    global cnt
    if n==0:
        return
    if n==1:
        path.append((f,t))
        cnt += 1
    else:    #위꺼 대피 - 출발지, 도착지 이외의 장소.
        hanoi(f,t,m,n-1)
        #맨 아래 꺼.
        hanoi(f,m,t,1)
        hanoi(m,f,t,n-1)

cnt=0
N = int(input())

hanoi(1,2,3,N)

print(cnt)
for x in path:
    print(x[0],x[1],sep=' ')
