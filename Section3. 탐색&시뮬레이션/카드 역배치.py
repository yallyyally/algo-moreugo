#카드 역배치
#정해진 구간만큼 역정렬,

def makeNewArr(arr):
    arr.reverse()
    return arr

arr = [0]*20
for i in range(20):
    arr[i] = i+1

for i in range(10):
    start,end= map(int,input().split())
    tmp = arr[start-1:end]
    arr[start-1:end] = makeNewArr(tmp)
for x in arr:
    print(x,end=' ')
