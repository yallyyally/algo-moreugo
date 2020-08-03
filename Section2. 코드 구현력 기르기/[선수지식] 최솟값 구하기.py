arr = [5,3,7,9,2,5,2,6]
arrMin=float('inf') #최솟값을 저장.-> 파이썬 내에서 제일 큰 값.
#arr[0] 해놓고 range(1,len(arr))해도 됨
for i in range(len(arr)): #for x in arr(inf로 초기화 했을 때)
    if arr[i]<arrMin: #x<ArrMin
        arrMin = arr[i] #arrMin=x

print(arrMin)