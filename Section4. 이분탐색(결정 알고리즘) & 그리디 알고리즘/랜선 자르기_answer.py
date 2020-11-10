import sys

#sys.stdin = open("in3.txt","rt")
#결정 알고리즘으로 풀 수 있는 문제 -> 답의 범위를 바로 알 수 있다.
##범위 내의 특정 숫자를 정해놓고 유효하냐, 아니냐를 확인함수로 확인함.-> 범위를 좁혀감..

# 랜선 한 개의 길이는 1~ 가장 큰 랜선의 길이 (802) 까지.-> 이 범위 내에서 이분탐색을 시도한다.

res = 0
cables = []
k=0

def binarySearch(start,end):
    if start>end:
        #끝
        print(res)
    else:
        temp_length = (start+end)//2
        temp = 0
        for x in cables:
            temp+= x//temp_length
        if temp > k :
            #임시적으로...
            res = temp_length
            #k보다 크니까 더 큰 크기로 나눠야 함 -> k와 같거나 (종료) 여전히 크지만 길이는 무족건 더 커짐
            #res 로 비교할 필요 X
            binarySearch(temp_length+1,end)
        elif temp==k:
            print(temp_length)
        else :
            #k보다 작으니까 더 작은 크기로 나눠야 함
            binarySearch(start,temp_length-1)

            #그 수가 k보다 큰 범위에서 최소임
N,k = map(int,sys.stdin.readline().split())

#N개의 랜선 k개로 균등하게 만들기

for _ in range(N):
    cables.append(int(sys.stdin.readline()))
cables.sort(reverse = True)

#1~max 사이의 값
max = cables[0]
binarySearch(1,max)

