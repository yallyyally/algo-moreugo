# -*- coding:utf-8 -*-
def solution(s):
    answer = True
    
    opener = ['(','{','[']
    closer = [')','}',']']
    
    stack = []
    
    for letter in s:
        if letter in opener:
            stack.append(letter)
        else:
            #if close-> check if stack is empty(no match)
            if len(stack)==0:
                answer = False
                break
            else: #something in the stack
                 #compare as index
                if closer.index(letter) != opener.index(stack.pop()):
                    answer = False
                    break
            
    #(((((-> No stay
    if len(stack) > 0:
        answer = False

    return answer

