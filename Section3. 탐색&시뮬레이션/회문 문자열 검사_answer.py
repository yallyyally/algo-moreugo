#회문 문자열 검사
#문자열 N개 입력받아서 회문이면 YES 회문 아니면 NO 출력
#대소문자 구분 X

N = int(input())
# ans = [0]*N #회문이면 1, 회문이 아니면 0

for i in range(N):
    x = input()
    x=x.lower() #다 소문자로 통일
    # ans[i] = test(x)
    size = len(x)
    for j in range(size//2):
        #5글자라면 0==4(-1),1==3(-2) 비교, 가운데는 냅둬
        if x[j]!=x[-1-j]:
            print("#%d NO"%(i+1))
            break
    else: # break 안당하고 정상종료 했을 때
        print("#%d YES" %(i+1))
    #####flag 쓰지 말고 for-else 활용하자!!####