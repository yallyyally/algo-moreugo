def binary(s,end,arr,M):
    #s: 시작 인덱스, end: 끝 인덱스, arr: 대상 배열, M: 찾는 수
    if end<s:
        print('-1')
        return
    avg = (s+end)//2
    if M==arr[avg]:
        #평균에 딱 있슴
        print(avg+1) #위치번호니까 1 더함
        #return avg 하면 자기 자신한테 리턴 해버림,,,,
        return
    elif M>arr[avg]:
        binary(avg+1,end,arr,M)
    else:
        binary(s,avg-1,arr,M)

#N,M 입력
N,M = map(int,input().split())
#arr 입력받고 정렬
arr = list(map(int,input().split()))
arr.sort()

binary(0,N-1,arr,M)