import sys

#sys.stdin = open("in3.txt","rt")
#finding between 1~max => through binary search.
##narrow down the ranges

def Count(len):
    #defines how many lanseons will appear and returns it.
    cnt = 0
    for x in Line:
        cnt+=x//len
    return cnt

N,k = map(int,sys.stdin.readline().split())

Line = []
res = 0 #maximum
largest = 0 #finding the largest lanseon -> the maximum territory
for i in range(N):
    tmp = int(input())
    Line.append(tmp)
    largest = max(largest,tmp)
    ##max: compares the two numbers and returns the bigger one
lt = 1
rt = largest

while lt<=rt:
    mid = (lt+rt)//2
    if Count(mid)>=k:
        res = mid
        lt = mid+1
    else:
        rt = mid-1

print(res)

