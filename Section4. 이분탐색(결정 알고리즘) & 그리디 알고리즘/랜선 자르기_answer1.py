import sys

#sys.stdin = open("in3.txt","rt")
#finding between 1~max => through binary search.
##narrow down the ranges


def binarySearch(start,end,res):
    if start>end:
        print(res)
    else:
        temp_length = (start+end)//2
        temp = 0
        for x in cables:
            temp+= x//temp_length
        if temp >= k :
            #next temp must be longer than res, so we don't have to compare res.
            res = temp_length
            binarySearch(temp_length+1,end,res)

        else :
            #as temp is smaller than k, it does not match with the condition.
            #res = temp_length -> this is a wrong condition, so we should not store res in here
            binarySearch(start,temp_length-1,res)

N,k = map(int,sys.stdin.readline().split())
cables = []
for _ in range(N):
    cables.append(int(sys.stdin.readline()))
cables.sort(reverse = True)

max = cables[0]
binarySearch(1,max,0)

