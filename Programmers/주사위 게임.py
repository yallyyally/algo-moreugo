# -*- coding:utf-8 -*-

import math

def solution(monster, S1, S2, S3):
    answer = -1
    
    #max값 알아보기 - 가장 멀리 있는 몬스터 maxMonster
    monster.sort(reverse = True)
    maxMonster = monster[0]
    
    #전체 경우의 수, 해당되는 경우의 수
    entire = S1 * S2 * S3
    case = 0
    
    #s1, s2, s3을 순차적으로 더하되, 중간에 (s1이나 s2에서) max보다 같거나 큰게 나오면 break
    for s1 in range(1, S1 + 1):
        total = s1 + 1 #1부터 시작
        if total >= maxMonster:
            break
        for s2 in range(1, S2 + 1):
            if total + s2 >= maxMonster:
                break
            total += s2
            for s3 in range(1, S3 + 1):
                if total + s3 > maxMonster:
                    break
                
                if total + s3 in monster:
                    case += 1
                
            total -= s2 #다른 s2 넣어야 함
            
    #case 다 구함
    case = entire - case
    print(entire, case)
    answer = math.floor(case / entire * 1000)
    print (answer)
    
    return answer

monster = [4, 9, 5, 8]
s1 = 2
s2 = 3
s3 = 3

print(solution(monster, s1, s2, s3))