N = int(input())
arr1 = list(map(int,input().split()))
M = int(input())
arr2 = list(map(int,input().split()))
arr = list()
#걍 합해서 sort 때리면 8log8, 머지 하면 8
#merge sort로 구현하기
i=j=0
while i<N and j<M:
    if arr1[i]<=arr2[j]:
        arr.append(arr1[i])
        i+=1
    else:
        arr.append(arr2[j])
        j+=1

if i>=N:
    #끝까지 합치기. for문 돌리지 말고 슬라이싱 붙이기!!
    arr = arr+arr2[j:]

else:
    arr = arr+arr1[i:]

for x in arr:
    print(x,end =' ')
