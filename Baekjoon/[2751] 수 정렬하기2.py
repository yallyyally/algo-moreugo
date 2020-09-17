import sys
numbers = [False]*2000001
#-1,000,000 -> 0
N = int(sys.stdin.readline().rstrip())

for _ in range(N):
    i = int(sys.stdin.readline())
    numbers[i+1000000] = True
cnt = 0
for i in range(len(numbers)):
    if numbers[i]==True:
        print(i-1000000)
        cnt+=1
        if cnt==N:
            break