import sys

#sys.stdin = open("in3.txt","rt")
#finding between 1~max => through binary search.
##narrow down the ranges

res = 0
cables = []
k=0

def binarySearch(start,end):
    if start>end:
        #��
        print(res)
    else:
        temp_length = (start+end)//2
        temp = 0
        for x in cables:
            temp+= x//temp_length
        if temp > k :
            #next temp must be longer than res, so we don't have to compare res.
            res = temp_length
            binarySearch(temp_length+1,end)
        elif temp==k:
            print(temp_length)
        else :
            #as temp is smaller than k, it does not match with the condition.
            binarySearch(start,temp_length-1)

N,k = map(int,sys.stdin.readline().split())


for _ in range(N):
    cables.append(int(sys.stdin.readline()))
cables.sort(reverse = True)

#1~max ������ ��
max = cables[0]
binarySearch(1,max)

