import sys

# 행, 열, 대각선 ->열 -> 열,대각선
# 행, 행,행, 행

N = int(sys.stdin.readline())
board = []
for i in range(N):
    board.append(list(map(int, sys.stdin.readline().rstrip().split())))

# 격자판 입력 완료
max = 0
sums = [0]*3

for i in range(N):
    #0. 각 행의 합
    if max<sum(board[i]):
        max = sum(board[i])
    if i==0:
        sum_l=0 #대각선(왼)
        sum_s=0 #대각선(오)
        for j in range(N):
            #1. 대각선 합
            sum_l +=board[j][j]
            #2. 대각선합 2
            sum_s+=board[j][N-1-j]

        sums[0],sums[1] = sum_l,sum_s
        sums.sort(reverse=True)

        if max < sums[0]:
            max= sums[0]
    #3.열의 합
    sums = 0
    for j in range(N):
        sums+=board[j][i]
    if max<sums:
        max = sums

print(max)
