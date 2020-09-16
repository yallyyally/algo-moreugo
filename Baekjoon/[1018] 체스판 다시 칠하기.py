import sys
sys.stdin=open("input.txt","rt")

def WhiteorBlack(b):
    #보드를 흰색부터 시작해서 채울 때 바꿔야 하는 것들 수 리턴
    #가로, 세로 두칸씩 띔
    #WB
    #BW
    i=0
    cnt = 0
    cnt_b=0
    while i<8:
        j=0
        while j<8:
            if b[i][j]!='W':
                cnt+=1
            else:
                cnt_b+=1
            if b[i][j+1]!='B':
                cnt += 1
            else:
                cnt_b+=1
            if b[i+1][j]!='B':
                cnt += 1
            else:
                cnt_b+=1
            if b[i+1][j+1]!='W':
                cnt += 1
            else:
                cnt_b+=1
            j+=2
        i+=2

    if cnt_b<cnt:
        return cnt_b
    else:
        return cnt


M,N = map(int,input().split())
##빠르게 이차원 배열 입력하는 법
board = [list(input().split()) for _ in range(M)]

for i in range(len(board)):
    #문자열 -> 문자 리스트
    board[i] = list(board[i][0])
#파싱 완료
i,j=0,0
min = 21470000
newBoard = [[0]*8 for _ in range(8)]


#ok
i = 0
# 보드판 스캔
while i+7<M:
    j=0
    #맨 밑 칸 추가
    for k in range(8): #8*7 칸 초기화
        newBoard[k][j:j + 7] = board[i+k][j:j + 7]

    while j+7<N:
        #뒤에거 들어옴
        for k in range (8):
            newBoard[k][7] = board[i+k][j+7]

        cand = WhiteorBlack(newBoard)
        if min>cand:
            min=cand

       #앞에꺼 나가고
        if j+1<N: #맨 끝이 아닐때만 추가,,
            for k in range(8):
                newBoard[k].pop(0)
                newBoard[k].append(0)
        j+=1
    #위에꺼 나가고
    i+=1
print(min)


