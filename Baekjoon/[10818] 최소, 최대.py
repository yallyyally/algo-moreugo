N = int(input())

arr = [0]*N
arr = list(map(int,input().split()))

arr.sort()
print(arr[0],arr[N-1],end=' ')