def fromWhilte(board):
    return 0
def fromBlack(board):
    return 0
M,N = map(int,input().split())
##빠르게 이차원 배열 입력하는 법
board = [list(map(int, input().split())) for _ in range(N)]

j,i = 0,0
min = 21470000
#전체 나무판때기 고려해서 새로 칠할 거 결정
while j+7<N and i+7<M:
    #보드판 스캔
        newBoard = board[]
        for k in range(i,i+7):
            for a in range(j,j+7):

