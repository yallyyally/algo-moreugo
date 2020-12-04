# -*- coding:utf-8 -*-
import heapq

def solution(no, works):
    result = 0

    works_inverse = []
    
    for x in works:
        works_inverse.append(x * (-1))
    
    heapq.heapify(works_inverse)
    
    while no>0 and sum(works_inverse)<0:

        root = heapq.heappop(works_inverse)
        heapq.heappush(works_inverse, root+1)
        no-=1
        
     
    for w in works_inverse:
        result+= abs(w) ** 2
    return result

n = 4
works = [4, 3, 3]
print(solution(n, works))