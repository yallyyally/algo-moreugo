 def solution(number, k):
     collected = []
     #N
     for i, num in enumerate(number): #i는 index, num은 value
         #number[i]==num
         #되도록이면 for문은 한번만 쓰자.
         #empty할 때도 봐줘야.
         #넣거나 / 말거나 한번에 처리, collected의 크기는 별로 안 중요. 
         #collected에서 나간 원소의 개수(k까지)만 중요
         
         #맨 마지막 것만 보는 이유 - while 돌리니까. 어차피 앞엔 더 큰 수 들 있음
         #한글자 문장은 그대로 비교해도 ㄱㅊ
         
         #빠지거나 (추가되거나)->전체 시간 복잡도가 N^2이 아닌 이유
         #K에 따라, collected의 길이에 따라 시행되지 않을 수도 있으므로 안쳐줌(초반의 경우)
         while len(collected) > 0 and collected[-1] < num  and k > 0:
                 collected.pop(-1)
                 k-=1
        if k==0:
            #슬라이스 된 것에서 끝날 게 아니라 리스트 화 해야 됨
            collected+=list(number[i:])
            break #종료
        #collected에 암것도 없거나, k 에 도달 했거나 이미 큰 수가 있으면 그냥 넣기
        #추가되거나
        collected.append(num) 
        '''
    while k>0:
        collected.pop(-1)
        k-=1
        '''
    collected = collected[:-k] if k>0 else collected
    
    answer = ''.join(collected)
    return answer