N = int(input())
#N*N 격자판
board =[]
for i in range(N):
    board[i] = list(map(input().split()))