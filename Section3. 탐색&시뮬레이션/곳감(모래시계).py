import sys
#sys.stdin = open("input.txt","rt")
def move(board,row,d,times,length):
    #board[row]를 d 방향으로 times 만큼 이동시켜
    ##board를 반환
    cols = []
    newBoard = [0]*length

    #변경 후 열의 위치 저장
    for i in range(length):
        cols.append(i)
    if d:#오른쪽
        for i in range(length):
            cols[i]+= times
            while cols[i]>length-1:
                cols[i]-=length

    else: #왼쪽
        for i in range(length):
            cols[i]-=times
            while cols[i]<0:
                cols[i]+=length

    #cols 배열을 바탕으로 board 재정비
    for i in range(length):
        newBoard[cols[i]] = board[row][i]

    board[row] = newBoard

    return board

#모래시계 영역 감 개수 출력
def countGam(board,length):
    #위, 아래 줄 초기화
    row_up = 0
    row_down = length-1
    #처음, 끝 인덱스 초기화
    s = 0
    e = length-1
    gam = 0
    while s!=e:
        gam+=sum(board[row_down][s:e+1])
        gam+=sum(board[row_up][s:e+1])
        row_up+=1
        row_down-=1
        s+=1
        e-=1

    gam+=board[row_down][s]
    print(gam)

#board 초기화
N = int(sys.stdin.readline())
board = []

for _ in range(N):
    board.append(list(map(int,sys.stdin.readline().split())))

#명령 입력
M = int(sys.stdin.readline())

for _ in range(M):
    row,d,times = map(int,(sys.stdin.readline().split()))
    board = move(board,row-1,d,times,N)

#모래시계 영역 출력
countGam(board,N)
