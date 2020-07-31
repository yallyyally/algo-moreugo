#소수(에라토스테네스 체)
#N 입력시 1~N 소수 출력

N = int(input())

list = [1]*(N+1)

#[2]부터 [N-1]까지
for i in range(2,N):
    #소수인 경우에만.. 지워진걸
    #조건검사하는 시간이 든다고 하지만 반복문 통째로 실행하는 것보다야 낫다.
    if list[i]:
        j=2
        #*2 *3 ... 하다가 N이 되기 전까지!
        while(i*j<=N):
        # while (i * j <= N and list[i * j]):
        #이게 틀린 이유: j=2,3,5..이렇게 곱해줘야 하는데
        #뭐하나라도 소수가 아니면 바로 다음 i로 넘어가버린다.
            # if(list[i*j]):
            list[i*j]=0
            j+=1

#[0],[1] 제외
print(sum(list)-2)