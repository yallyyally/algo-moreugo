# -*- coding:utf-8 -*-

def solution(skill, skill_trees):
    answer = 0
    stack = []
    
    prior = {}
    #우선순위 딕셔너리로 정리
    for i,s in enumerate(skill):
        prior[s] = i
    
    for sk in skill_trees:
        stack.clear()
        for s in sk:
            #한 알파벳씩
            # 스택이 비어있다면 - 스킬 있으면 넣긔.
            ##아무 것도 없다면 가장 우선 순위인 것만 허용
            if s in prior.keys():
                if len(stack)==0 and prior[s] == 0:
                    stack.append(s)
                elif len(stack)==0 and prior[s]>0:
                    break
                # 스택 안 빔 - 스킬 있고 && 우선순위 가능한거 넣긔
                elif len(stack) and prior[stack[-1]] == prior[s] - 1:
                    stack.append(s)
                else:
                    break
        else:
            answer+=1
            
    return answer