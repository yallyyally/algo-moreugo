#카드 역배치
#정해진 구간(s,e)만큼 역정렬,
import sys
sys.stdin = open("input.txt", "r")

def makeReverse(arr,s,e):
    arr2 = arr[s-1:e]
    return reversed(arr2)

arr = []
#배열 초기화
for i in range(20):
    arr.append(i+1)
dict = {}

#입력값 받기
for _ in range(10):
    #tuple로 저장
    s,e = map(int,input().split())
    #손상X, 두번 연속 -> 실행X
    #시작점이 끝점보다 같거나 작으면 손상 ->실행해야 함.
    #시작점과 끝점이 모두 같고 손상X, 같은것의 개수가 짝수 -> 실행x
    for x in dict.keys():
        print(x)
        if x==(s,e): #같은것 발견
            #손상됐음 pass
            if dict.get(x,0)==0:
                 #손상됐으므로 실행해야 함
                break
            #손상 안됐으면
            else:
                dict[x]+=1
                break
        else: #같은건 없음
            #시작점이 끝점보다 같거나 작으면 손상..
            if s<=x[1]:
                dict[(s,e)] = 0
                dict[x] = 0
                break
    else: #brak안하고 끗남 ->같은것도 없었고, 손상도 안시킨 독립
        dict[(s,e)] = 1

for x in dict:
    if dict[x]%2:
        arr[x[0]-1:x[1]] = makeReverse(arr,x[0],x[1])
print(arr)