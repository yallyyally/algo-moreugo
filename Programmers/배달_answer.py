
# -*- coding:utf-8 -*-
from queue import PriorityQueue # 우선순위 큐

def dijkstra(road, N):
    queue = PriorityQueue()
    queue.put([1, 0])
    INF = 5000011
    dist = [INF] * (N + 1)
    dist[1] = 0
    
    while not queue.empty():
        current, current_cost = queue.get()
        
        for src, dest, cost in road:
            if src == current:
                if dist[dest] > current_cost + cost:
                    dist[dest] = current_cost + cost
                    queue.put([dest, current_cost + cost])
            elif dest == current:
                if dist[src] > current_cost + cost:
                    dist[src] = current_cost + cost
                    queue.put([src, current_cost + cost])
    return dist
    
def solution(N, road, K): #road 조건에서 N개의 마을, K시간 이하로 갈 수 있는 경우의 수
    dist = dijkstra(road, N)
    #for문으로 또 세고 있지 말 것.
    return len([x for x in dist if x<= K])
