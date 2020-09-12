T = int(input())

for _ in range(T):
    #N 입력
    N = int(input())
    #N일 동안의 매매가 입력
    prices = list(map(int,input().split()))
    #최대 이익 출력