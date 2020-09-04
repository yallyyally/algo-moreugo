N = int(input())
arr1 = list(map(int,input().split()))
M = int(input())
arr2 = list(map(int,input().split()))
arr = list()
#merge sort로 구현하기
i,j=0,0
while i<len(arr1) and j<len(arr2):
    if arr1[i]<=arr2[j]:
        arr.append(arr1[i])
        i+=1
    else:
        arr.append(arr2[j])
        j+=1

if i>=len(arr1):
    while j<len(arr2):
        arr.append(arr2[j])
        j+=1
else:
    while i<len(arr1):
        arr.append(arr1[i])
        i+=1
for x in arr:
    print(x,end =' ')
