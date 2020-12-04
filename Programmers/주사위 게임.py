# -*- coding:utf-8 -*-

import math

def solution(monster, S1, S2, S3):
    answer = -1
    
    #max�� �˾ƺ��� - ���� �ָ� �ִ� ���� maxMonster
    monster.sort(reverse = True)
    maxMonster = monster[0]
    
    #��ü ����� ��, �ش�Ǵ� ����� ��
    entire = S1 * S2 * S3
    case = 0
    
    #s1, s2, s3�� ���������� ���ϵ�, �߰��� (s1�̳� s2����) max���� ���ų� ū�� ������ break
    for s1 in range(1, S1 + 1):
        total = s1 + 1 #1���� ����
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
                
            total -= s2 #�ٸ� s2 �־�� ��
            
    #case �� ����
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