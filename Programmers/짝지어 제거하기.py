def solution(s):
    answer = 0

    stack = []
    
    for alphabet in s:
        #check len
        if len(stack)==0:
            stack.append(alphabet)
        else:
            #something
            if stack[-1] == alphabet:
                #pop if same
                stack.pop()
            else:
                stack.append(alphabet)
    
    if len(stack)==0:
        answer = 1
    return answer