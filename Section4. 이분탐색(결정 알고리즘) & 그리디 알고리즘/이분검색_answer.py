#재귀함수 호출이 아닌 while문으로 간단하게 구현함 s<=end 를 while문 조건에 넣을 수도 있군,,
#시간: logN
#N,M 입력
N,M = map(int,input().split())
#arr 입력받고 정렬
arr = list(map(int,input().split()))
arr.sort()
s = 0
end = N-1
while s<=end:
    avg = (s+end)//2
    if M==arr[avg]:
        print(avg+1)
        break
    elif M> arr[avg]:
        s = avg+1
    else:
        end = avg-1
