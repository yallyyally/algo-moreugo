#회문 문자열 검사
#문자열 N개 입력받아서 회문이면 YES 회문 아니면 NO 출력
#대소문자 구분 X
##더 짧은 코드

N = int(input())
# ans = [0]*N #회문이면 1, 회문이 아니면 0

for i in range(N):
    x = input()
    x=x.lower() #다 소문자로 통일
    # ans[i] = test(x)
    if x==x[::-1]: #s[::-1]은 문자열을 뒤집는 코드
        print("#%d YES"%(i+1))
    else:
        print("#%d NO"%(i+1))

