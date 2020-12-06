def solution(board):
    answer = 0
    
    N = len(board)
    stack = [] #���⿡ ��� ����
    
    state = 0 #���θ� 0, ���θ� 1
    pos = [[1,1],[1,2],0] #�� ��ġ #pos[2]�� ���� �� ����.
    
    stack.append([[1,1],[1,2],0])
    #�� ��ġ �Բ� �ʱ�ȭ
    newBoard = [[1] * (N+2) for _ in range(N+1)]
    for i in range(1,N+1): #1-N
        newBoard[i][1:N+1] = board[i-1]
    
    while pos != [N,N]:
        tmp = []
        if state == 0 and pos[2] == 0: #�κ��� ������, ���η� ���� ��
            #pos[0]�� pos[1]�� �տ� ���� �ִ� �� ã��
            if pos[0][1] > pos[1][1]: 
                #pos[0]�� ����
                #���η� �� �� �ֳ�?
                if newBoard[pos[0][0]][pos[0][1] + 1 ]==0:
                    #���� ����
                    pos[0][1] += 1
                    pos[1][1] += 1
                    pos[2] = 0
                    tmp = pos
                    stack.append(tmp)
                    answer+=1
                else:
                    #ȸ���ؾ� ��
                    pos[2] = 1
            
            else:
                #pos[1]�� ����
                #���η� �� �� �ֳ�?
                if newBoard[pos[1][0]][pos[1][1] + 1] ==0:
                    #���� ����
                    pos[0][1] += 1
                    pos[1][1] += 1
                    pos[2] = 0
                    tmp = pos
                    stack.append(tmp)
                    answer+=1
                else:
                    #ȸ���ؾ� ��
                    pos[2] = 1
                
        elif state == 0 and pos[2] == 1: #�κ��� �����ε� ���η� ���� ��
            #���� ã��
            #���� 0
            if pos[0][1] > pos[1][1] : 
                if newBoard[pos[1][0] +1][pos[1][1]] ==0 and newBoard[pos[1][0]+1][pos[1][1]+1]==0:
                    #ȸ�� ����
                    pos[1][0]+=1
                    pos[1][1]+=1
                    tmp = pos
                    stack.append(tmp)
                    state = (state+1)%2
                    answer+=1
                else: #���� �����µ� ȸ���� �Ұ� - �ڷ� ����.(���� ���η� ���� ��) pop �ϰ� top pos[2] ��ġ��
                    stack.pop()
                    pos = stack[-1]
                    stack[-1][2] = (stack[-1][2]+1)%2
                    pos[2] = (pos[2]+1)%2
            else: #���� 1
                if newBoard[pos[0][0] +1][pos[0][1]] ==0 and newBoard[pos[0][0]+1][pos[0][1]+1]==0:
                    #ȸ�� ����
                    pos[0][0]+=1
                    pos[0][1]+=1
                    tmp = pos
                    stack.append(pos)
                    state = (state+1)%2

                    answer+=1
                else: #���� �����µ� ȸ���� �Ұ� - �ڷ� ����.(���� ���η� ���� ��) pop �ϰ� top pos[2] ��ġ��
                    stack.pop()
                    pos = stack[-1]
                    stack[-1][2] = (stack[-1][2]+1)%2

                    pos[2] = (pos[2]+1)%2
                
        elif state == 1 and pos[2] == 1: #�κ��� �����̰� ���η�
            #pos[0]�� pos[1]�� �ؿ� ���� �ִ� �� ã��
            if pos[0][0] > pos[1][0]: 
                #pos[0]�� ����
                #���η� �� �� �ֳ�?
                if newBoard[pos[0][0]+1][pos[0][1]]==0:
                    #���� ����
                    pos[0][0] += 1
                    pos[1][0] += 1
                    pos[2] = 1
                    tmp = pos
                    stack.append(pos)
                    answer+=1
                else:
                    #ȸ���ؾ� ��
                    pos[2]  = (pos[2]+1)%2
            
            else:
                #pos[1]�� ����
                #���η� �� �� �ֳ�?
                if newBoard[pos[1][0]+1][pos[1][1] ] ==0:
                    #���� ����
                    pos[0][0] += 1
                    pos[1][0] += 1
                    pos[2] = 1
                    tmp = pos
                    stack.append(pos)
                    answer+=1
                else:
                    #ȸ���ؾ� ��
                    pos[2] = (pos[2]+1)%2
                    
        elif state == 1 and pos[2] == 0: #�κ��� �����ε� ���η� ���� ��
            #���� ã��
            #���� 0
            if pos[0][0] > pos[1][0] : 
                if newBoard[pos[1][0]][pos[1][1]-1] ==0 and newBoard[pos[1][0]+1][pos[1][1]-1]==0:
                    #ȸ�� ����
                    pos[1][0]+=1
                    pos[1][1]-=1
                    tmp = pos
                    stack.append(pos)
                    state = (state+1)%2

                    answer+=1
                else: #���� �����µ� ȸ���� �Ұ� - �ڷ� ����.(���� ���η� ���� ��) pop �ϰ� top pos[2] ��ġ��
                    stack.pop()
                    pos = stack[-1]
                    stack[-1][2] = (stack[-1][2]+1)%2
                    pos[2] = (pos[2]+1)%2
            else: #���� 1
                if newBoard[pos[0][0] ][pos[0][1]-1] ==0 and newBoard[pos[0][0]+1][pos[0][1]-1]==0:
                    #ȸ�� ����
                    pos[0][0]+=1
                    pos[0][1]-=1
                    tmp = pos
                    stack.append(pos)
                    state = (state+1)%2
                    answer+=1
                else: #���� �����µ� ȸ���� �Ұ� - �ڷ� ����.(���� ���η� ���� ��) pop �ϰ� top pos[2] ��ġ��
                    stack.pop()
                    pos = stack[-1]
                    stack[-1][2] = (stack[-1][2]+1)%2
                    pos[2] = (pos[2]+1)%2 
    
    
    return answer
board = [[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]]
print(solution(board))