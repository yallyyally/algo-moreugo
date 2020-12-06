# -*- coding:utf-8 -*-

import queue

visited = []
answer = 0

def bfs(i, j, image,q):
    #방문이 안되어서 solution에 의해 왔거나, 다른 것에 의해 이어져서 bfs에서 왔거나
    global visited
    global answer
    
    color = q.get()
   
    #i행 j열 이후를 탐색
    next_j = j+1
    next_i = i+1
    
    #위, 아래, 왼, 오른쪽(범위내)를 탐색
    #만약 이미 방문 된 것 들중 나랑 색이 같음 -> 오른쪽, 아래가 본래 같은 색이었음, 떨어져 있는 게 아니었음.

    ##오른쪽만, 아래쪽 오른쪽 둘다, 아래쪽만
    if next_j < len(image[i]) and image[i][next_j] == color:     
        if visited[i][next_j] == 0 :
            #색깔이 같은 경우만 계속 이어 나감
            visited[i][next_j] = 1
            q.put(image[i][next_j])
            
            #아래 쪽 && 오른쪽
            if next_i < len(image) and visited[next_i][j] == 0:
                if image[next_i][j] == color:
                    visited[next_i][j] = 1
                    q.put(image[next_i][j])          
                    bfs(i, next_j, image,q)
            else: #오른쪽만
                if next_i < len(image) and visited[next_i][j] == 1:
                    if image[next_i][j] == color:
                        answer -= 1
            bfs(i, next_j, image,q)

    #아래쪽만
    elif next_i < len(image) and image[next_i][j] == color:     
        if visited[next_i][j] == 0:
            #색깔이 같은 경우만 계속 이어 나감
            visited[next_i][j] = 1
            q.put(image[next_i][j])
            bfs(next_i,j,image,q)
        else:
            if image[next_i][j] == color:
                answer -= 1


    #오른쪽 왼쪽 다 범위 밖이거나, 다 색깔 다른 경우는 탐색 중지.
    #1색 1큐
    
    
def solution(n, m, image):
    global answer
    global visited
    visited = [[0]*m for _ in range(n)]

    
    for i in range(n):
        for j in range(m):
            #방문하지 않았으면 ++하고 재귀 ㄱ
            if visited[i][j] == 0:
                q = queue.Queue()
                answer += 1
                visited[i][j] = 1
                q.put(image[i][j])
                bfs(i, j, image,q)
           
    return answer