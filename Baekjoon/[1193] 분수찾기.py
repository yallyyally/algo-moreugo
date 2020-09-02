
N = int(input())

'''
원점(1)
오른 대각선아래 아래 대각선위*2 (2)
오른, 대각선아래*3, 아래,대각위*4, (3)
오른, 대각아래 *5 ,아래, 대각위 *6 (4)
오른 ...
'''
#1. 몇번째 그룹인가?
i = 1
k = 1
g = 1

while i<N:
    i += k
    k += 4
    g += 1


bj = 1
#오른 이후
if i!=N:
    #원상복구
    g-=1
    i-=k-4
    bm = (g-1)*2

    if N<=i+2*(g-1)-1:
        bm-=N-i
        bj+=N-i
    elif N==i+2*(g-1):
        bj = bm+1
        bm=1
    else:
        bj = bm+1
        bj-=N-i-2*(g-1)
        bm=1
        bm+=N-i-2*(g-1)

else:
    if g!=1:
        bm = 2*(g-1)
    else:
        bm=1
print(bj,bm,sep='/')