import sys
#sys.stdin = open("input.txt","rt")



board=[]
for _ in range(7):
    board.append(list(map(int,sys.stdin.readline().split())))
b= []
cnt = 0
for i in range(7):
    for j in range(7):
        #1. 세로 회문
        if i+4<7:
            b.clear()
            for k in range(5):
                b.append(board[i+k][j])
            if b[::-1]==b:
                cnt+=1
        #2. 가로 회문
        if j+4<7:
            b.clear()
            for k in range(5):
                b.append(board[i][j+k])
            if b[::-1]==b:
                cnt+=1

print(cnt)