#Music Video
##share the package to minimize the difference

import sys

EqualSum = 0

def diffBetAvg(num):
    global EqualSum
 
    return abs(EqualSum - num)

N,M = map(int,sys.stdin.readline().split())
Length = list(map(int,sys.stdin.readline().split()))

#initialize size
EqualSize = N//M
EqualSum = sum(Length)//M

lt = [0]*M
rt = [0]*M
diff = [0]*M
diff_abs = [0]*M
maxDiff  = -1
indexMaxDiff = -1

#initialize each size
for i in range(M):
    lt[i] = i*EqualSize
    rt[i] = lt[i]+EqualSize
#last territy
rt[M-1] = len(Length)

#check if there is anything changed
flag = 1
#############합 + 서로간의 차이도 고려##################################
while flag:
    flag = 0
    maxDiff = -1
    indexMaxDiff = -1
    #find the differnece between sum(eachpack) &EqualSum
    for i in range(M):
        diff[i] = sum(Length[lt[i]:rt[i]]) - EqualSum
        diff_abs[i] = abs(diff[i])
        if diff_abs[i]>maxDiff:
            maxDiff= diff_abs[i]
            indexMaxDiff = i

    #modify the maximum diff package
    if diff[indexMaxDiff]>0:
        sumofDiff = sum(diff_abs)

        #we should reduce the difference to nearly 0
        if indexMaxDiff==0 :
            #move the next one if it exists
            makeRightBigger = sum(Length[lt[indexMaxDiff]:rt[indexMaxDiff]-1])
            rightGotBigger = sum(Length[lt[indexMaxDiff+1]-1:rt[indexMaxDiff+1]])
            diff_abs[indexMaxDiff] = diffBetAvg(makeRightBigger)
            diff_abs[indexMaxDiff+1] = diffBetAvg(rightGotBigger)
            ###해당 묶음의 변화만 보지 말고, 변화된 이후의 diff_abs 배열 sum이랑 변화하기 전 diff_abs 배열 sum으로 둬야 함.
            if sumofDiff>sum(diff_abs):
                #change the territory
                rt[indexMaxDiff]-=1
                lt[indexMaxDiff+1]-=1
                flag = 1
            elif sumofDiff==sum(diff_abs):
                #이 경우는 둘 사이의 차이가 적은 쪽으로
                if abs(rightGotBigger - makeRightBigger)<abs(sum(Length[lt[indexMaxDiff]:rt[indexMaxDiff]])-sum(Length[lt[indexMaxDiff+1]:rt[indexMaxDiff+1]])):
                    rt[indexMaxDiff]-=1
                    lt[indexMaxDiff+1]-=1
                    flag = 1

        elif indexMaxDiff==M-1 :
            #move the previous one if it exists
             makeLeftBigger = sum(Length[lt[indexMaxDiff]+1:rt[indexMaxDiff]])
             leftGotBigger = sum(Length[lt[indexMaxDiff-1]:rt[indexMaxDiff-1]+1])
             diff_abs[indexMaxDiff] = diffBetAvg(makeLeftBigger)
             diff_abs[indexMaxDiff-1] = diffBetAvg(leftGotBigger)
             if sumofDiff>sum(diff_abs):
                 lt[indexMaxDiff]+=1
                 rt[indexMaxDiff-1]+=1
                 flag = 1
             elif sumofDiff==sum(diff_abs):
                #둘 차이가 적은 쪽으로
                 if abs(makeLeftBigger - leftGotBigger)<abs(sum(Length[lt[indexMaxDiff-1]:rt[indexMaxDiff-1]]) - sum(Length[lt[indexMaxDiff]:rt[indexMaxDiff]])):
                    lt[indexMaxDiff]+=1
                    rt[indexMaxDiff-1]+=1
                    flag =1

        else: #choose to move the previous one OR next one
            makeLeftBigger = sum(Length[lt[indexMaxDiff]+1:rt[indexMaxDiff]])
            makeRightBigger = sum(Length[lt[indexMaxDiff]:rt[indexMaxDiff]-1])
            rightGotBigger = sum(Length[lt[indexMaxDiff+1]-1:rt[indexMaxDiff+1]])
            leftGotBigger = sum(Length[lt[indexMaxDiff-1]:rt[indexMaxDiff-1]+1])
            #왼쪽을 키웠을때의 diff_abs
            diff_abs_left = sum(diff_abs[0:indexMaxDiff-1])+diffBetAvg(leftGotBigger)+diffBetAvg(makeLeftBigger)+sum(diff_abs[indexMaxDiff+1:M])
            #오른쪽을 키웠을 때의 diff_abs
            diff_abs_right = sum(diff_abs[0:indexMaxDiff]+diffBetAvg(makeRightBigger)+diffBetAvg(rightGotBigger)+sum(diff_abs[indexMaxDiff+2:M]))


            if diff_abs_right<diff_abs_left: 
                if diff_abs_right<sumofDiff:
                #makeRight Bigger
                    rt[indexMaxDiff]-=1
                    lt[indexMaxDiff+1]-=1
                    flag = 1
                elif diff_abs_right==sumofDiff:
                    if abs(makeRightBigger-rightGotBigger)<abs(sum(Length[lt[indexMaxDiff]:rt[indexMaxDiff]])-sum(Length[lt[indexMaxDiff+1]:rt[indexMaxDiff+1]])):
                        rt[indexMaxDiff]-=1
                        lt[indexMaxDiff+1]-=1
                        flag = 1
            elif diff_abs_right>diff_abs_left:
               if diff_abs_left<sumofDiff:
                #makeLeftBigger
                   lt[indexMaxDiff]+=1
                   rt[indexMaxDiff-1]+=1
                   flag = 1
               elif diff_abs_left==sumofDiff:
                   if abs(makeLeftBigger-leftGotBigger)<abs(sum(Length[lt[indexMaxDiff]:rt[indexMaxDiff]])-sum(Length[lt[indexMaxDiff-1]:rt[indexMaxDiff-1]])):
                       lt[indexMaxDiff]+=1
                       rt[indexMaxDiff-1]+=1
                       flag =1


            

    elif diff[indexMaxDiff]<0:
        #we should increase the difference to nearly 0
        sumofDiff = sum(diff_abs)

        if indexMaxDiff==0:
            #reduce the next one
            makeRightSmaller = sum(Length[lt[indexMaxDiff]:rt[indexMaxDiff]+1])
            rightGotSmaller = sum(Length[lt[indexMaxDiff+1]+1:rt[indexMaxDiff+1]])
            diff_abs[indexMaxDiff] = diffBetAvg(makeRightSmaller)
            diff_abs[indexMaxDiff+1] = diffBetAvg(rightGotSmaller)
            if sumofDiff>sum(diff_abs):
                rt[indexMaxDiff]+=1
                lt[indexMaxDiff+1]+=1
                flag = 1
            elif sumofDiff==sum(diff_abs):
                if abs(makeRightSmaller - rightGotSmaller)<abs(sum(Length[lt[indexMaxDiff]:rt[indexMaxDiff]])-sum(Length[lt[indexMaxDiff+1]:rt[indexMaxDiff+1]])):
                    rt[indexMaxDiff]+=1
                    lt[indexMaxDiff+1]+=1
                    flag = 1

        elif indexMaxDiff==M-1 :
            #reduce the previous one
             makeLeftSmaller = sum(Length[lt[indexMaxDiff]-1:rt[indexMaxDiff]])
             leftGotSmaller = sum(Length[lt[indexMaxDiff-1]:rt[indexMaxDiff-1]-1])
             diff_abs[indexMaxDiff] = diffBetAvg(makeLeftSmaller)
             diff_abs[indexMaxDiff-1] = diffBetAvg(leftGotSmaller)
             if sumofDiff>sum(diff_abs):
                 lt[indexMaxDiff]-=1
                 rt[indexMaxDiff-1]-=1
                 flag = 1
             elif sumofDiff==sum(diff_abs):
                 if abs(makeLeftSmaller - leftGotSmaller)<abs(sum(Length[lt[indexMaxDiff-1]:rt[indexMaxDiff-1]]) - sum(Length[lt[indexMaxDiff]:rt[indexMaxDiff]])):
                     lt[indexMaxDiff]-=1
                     rt[indexMaxDiff-1]-=1
                     flag = 1

        else: #choose to move the previous one OR next one
            makeRightSmaller = sum(Length[lt[indexMaxDiff]:rt[indexMaxDiff]+1])
            rightGotSmaller = sum(Length[lt[indexMaxDiff+1]+1:rt[indexMaxDiff+1]])
            makeLeftSmaller = sum(Length[lt[indexMaxDiff]-1:rt[indexMaxDiff]])
            leftGotSmaller = sum(Length[lt[indexMaxDiff-1]:rt[indexMaxDiff-1]-1])
            #왼쪽을 줄였을때의 diff_abs
            diff_abs_left = sum(diff_abs[0:indexMaxDiff-1])+diffBetAvg(leftGotSmaller)+diffBetAvg(makeLeftSmaller)+sum(diff_abs[indexMaxDiff+1:M])
            #오른쪽을 줄였을 때의 diff_abs
            diff_abs_right = sum(diff_abs[0:indexMaxDiff])+diffBetAvg(makeRightSmaller)+diffBetAvg(rightGotSmaller)+sum(diff_abs[indexMaxDiff+2:M])
            if diff_abs_right<diff_abs_left:
               if diff_abs_right<sumofDiff:
               #makeRight Smaller
                   rt[indexMaxDiff]+=1
                   lt[indexMaxDiff+1]+=1
                   flag = 1
               elif diff_abs_right == sumofDiff:
                   if abs(makeRightSmaller - rightGotSmaller)<abs(sum(Length[lt[indexMaxDiff]:rt[indexMaxDiff]]) - sum(Length[lt[indexMaxDiff+1]:rt[indexMaxDiff+1]])):
                       rt[indexMaxDiff]+=1
                       lt[indexMaxDiff+1]+=1
                       flag =1

            elif diff_abs_left<diff_abs_right:
               if diff_abs_left<sumofDiff:
                #makeLeft Smaller
                   lt[indexMaxDiff]-=1
                   rt[indexMaxDiff-1]-=1
                   flag = 1
               elif diff_abs_left==sumofDiff:
                   if abs(makeLeftSmaller - leftGotSmaller)<abs(sum(Length[lt[indexMaxDiff]:rt[indexMaxDiff]])-sum(Length[lt[indexMaxDiff-1]:rt[indexMaxDiff-1]])):
                       lt[indexMaxDiff]-=1
                       rt[indexMaxDiff-1]-=1
                       flag = 1
            
    


res = 0
for i in range(M):
    total = sum(Length[lt[i]:rt[i]])
    if res<total:
        res = total
    
print(res)


        


