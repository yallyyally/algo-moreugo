import sys
numbers = [False]*1000000

N = int(sys.stdin.readline().rstrip())

for _ in range(N):
    numbers[int(sys.stdin.readline().rstrip())] = True

for i in range(len(numbers)):
    if numbers[i]==True:
        print(i)