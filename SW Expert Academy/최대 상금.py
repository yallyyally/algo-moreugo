#최대 상금 -> 실패,,
'''
입력: 
테스트케이스 수
카드배열 교환횟수

출력:
#테스트케이스 번호 최대 금액
'''
def maximizeArray(card,times):
    #정해진 횟수만큼은 반드시 교환해야,
    for t in range(times):
        #인덱스 내에서 해결(더 커짐)

        for i in range(len(card)-1):
        #앞에서부터 이동
            #i 오른쪽에 있는 것들 중 제일 큰 것
            j=len(card)-1
            max = card[j]
            maxIndex = j
            while(j>=i+1):
                if card[j]>max:
                    max = card[j]
                    maxIndex = j
                j-=1

            #i보다 클 경우만 바꾸기.
            if card[i]<max :
                    card[i],card[maxIndex] = card[maxIndex],card[i]
                    break
        #인덱스 넘어갈 경우(강제로 바꿈 ->영향 최소화)
        else:
            card[len(card)-1],card[len(card)-2] = card[len(card)-2],card[len(card)-1]
    return card

def calculatePrice(card):
    #1,2,3,4,5->12345
    sum=0
    for i in range(len(card)):
        sum+=int(card[i])*10**(len(card)-1-i)
    print(sum)
    return sum

def findMaxPrice(card,times):
    #card를 times만큼 이동

    #1234->1,2,3,4
    card = list(str(card))
    for x in card:
        x = int(x)

    #최대 상금 계산
    card = maximizeArray(card, times)
    return calculatePrice(card)


T = int(input())
answers = [0]*T

for i in range(T):
    card,times = map(int,input().split())
    answers[i] = findMaxPrice(card,times)

print(answers)