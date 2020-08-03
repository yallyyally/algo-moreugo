#회문 문자열 검사
#문자열 N개 입력받아서 회문이면 YES 회문 아니면 NO 출력
#대소문자 구분 X

def test(x):
    #문자열 x가 회문이면 1 회문이 아니면 0 리턴
    org=x
    x= list(x)
    x.reverse()
    #list를 str화 하면 [이랑 ' '까지들어가므로 그냥 str을 list화 하자!

    if x==list(org):
        return 1
    else:
        return 0

N = int(input())
ans = [0]*N #회문이면 1, 회문이 아니면 0

for i in range(N):
    x = input()
    x=x.lower() #다 소문자로 통일
    ans[i] = test(x)

for i in range(N):
    print('#',i+1,end=' ')
    if ans[i]:
        print("YES")
    else:
        print("NO")