#-*- coding: utf-8 -*-
def solution(numbers):
    answer = ''
    numbers_new = [None]*len(numbers)
    #1. �� ���ڿ� ���·� �ٲ��ֱ�
    for i in range(len(numbers)):
        numbers_new[i] = [str(numbers[i]), i] #���� �ε����� ���� ����
        
    #2.�� ���ڸ����� �ٲ� - �ڸ��� ���ڶ�� �� ���ڸ� �����ϴ� ���
    for i in range(len(numbers)):
        for j in range(4-len(numbers_new[i][0])):
            numbers_new[i][0]+=numbers_new[i][0][len(numbers_new[i][0])-1]
    #�װ��� Ű�� ����
    numbers_new.sort(key = lambda x:(int(x[0][0]), int(x[0][1]), int(x[0][2]), int(x[0][3])), reverse = True)
    for n in numbers_new:
        answer+=str(numbers[n[1]])
    return answer

numbers = [3, 30, 34, 5, 9]
print(solution(numbers))