import sys

def countTop(board,N):
    #봉우리 수 리턴
    cnt=0
    for i in range(1,N+1):
        j=1
        while j<N+1:
            around = list((board[i-1][j],board[i+1][j],board[i][j-1],board[i][j+1]))
            if all (x<board[i][j] for x in around ):
                cnt+=1
                j+=2
            else:
                j+=1
    return cnt

N = int(sys.stdin.readline())

board = [[0]*(N+2) for _ in range(N+2)]
for i in range(1,N+1):
    board[i][1:N+1] = list(map(int,sys.stdin.readline().split()))
#보드 입력 완료

print(countTop(board,N))