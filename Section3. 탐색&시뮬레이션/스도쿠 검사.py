import sys
#sys.stdin = open("input.txt","rt")

board = []


for _ in range (9):
    board.append(list(map(int,sys.stdin.readline().split())))


flag = 0
s = list(i for i in range(1,10))
b = []
j=0
for i in range(9):
    # 1.행 검사
    if s != sorted(board[i]):
        flag = 1
        break

    for j in range(9):
        #중복검사 -> 집합 이용
        #열검사
        if i==1:
            b.clear()
            for k in range(9):
                b.append(board[k][j])
            if s!=sorted(b):
                flag=1
                break

        #칸검사 ->0,3,6
        if i%3==0 and j%3==0:
            b.clear()
            for k in range(3):
                for a in range(3):
                    b.append(board[i+k][j+a])
            if s!=sorted(b):
                flag=1
                break

    if flag:
        break

if flag:
    print("NO")
else:
    print("YES")