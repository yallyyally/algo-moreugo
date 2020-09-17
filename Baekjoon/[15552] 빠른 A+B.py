import sys
#sys.stdin.readline -> str, 한 글자씩, strip ㄱㄴ
#sys.stdin ->io.wrapper, 한 문장/str로 변환, strip 안됨
#split: 문자열을 띄어쓰기 기준으로 나눠서 리스트로 만들어줌.
T = int(sys.stdin.readline())
for _ in range(T):
    A,B=map(int,(sys.stdin.readline().split()))
    print(A+B)

