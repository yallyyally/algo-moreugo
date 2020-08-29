# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
# 총 노드 수 , 경로 수
graph = list()
max = 21470000

def draw_graph(a, c, cost):
    graph[a][c] = cost


N, M = map(int, input().split())
#initialize graph...
graph = [[21470000] * (M + 1) for i in range(M + 1)]
for i in range(len(graph)+1):
    graph[i][i]=0

#initialize distance: source to the point
    dist = [21470000]*(N+1)
    dist[1] = 0
#initialize visited
    visited = [0]*(N+1)
    visited[1]=1
#filling informations...
for _ in range(M):
    a, c, cost = map(int, input().split())
    draw_graph(a, c, cost)
    if a==1:
        dist[c] = cost

######SETTING UP

#finding shortest path
for i in range(1,N+1):
    for j in range(1,N+1):
        if graph[i][j]!=21470000:
            dist[j] = dist[w
    #1->i vs 1->j->i
if dist[i]>dist[j]+graph[j][i]