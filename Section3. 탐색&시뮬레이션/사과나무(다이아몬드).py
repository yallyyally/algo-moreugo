import sys
'''
N -> (N//2)+1 한 줄
    ->(시작점-1)(끝점-1)
    (시작점<끝점이 되면 break)
'''

N = int(sys.stdin.readline())
board = list(list() for _ in range(N))

for i in range(N):
    board[i] = list(map(int,sys.stdin.readline().split()))
#입력완료

#s,e 초기화
#row초기화

row = N//2
row_up = row-1
row_down = row+1
total = sum(board[row])
s,e = 1,N-2
while e>=s:
    total+=sum(board[row_up][s:e+1])
    total += sum(board[row_down][s:e+1])
    row_up-=1
    row_down+=1
    s+=1
    e-=1

print(total)