import sys

sys.stdin = open("input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    #빌딩 정보 입력
    N=int(input())
    buildings=list(map(int,input().split()))
    cnt=0
    #빌딩 한채 한채 검사
    for i in range(2,N-2):
        left_cnt = 0

        #왼쪽 조망권
        left=buildings[i]-buildings[i-1]
        left_left=buildings[i]-buildings[i-2]

        #왼쪽 두개 다 조망권 확보된 경우만 해당
        if left<=0 or left_left<=0:
        #둘 중 하나라도 0과 같거나 작으면 이미 그 집 조망권 x
            continue
        else:
            #왼쪽 조망권은 살아있다.->둘 중 작은 것.
            left_cnt=left if left<=left_left else left_left

        #오른쪽 조망권
        right=buildings[i]-buildings[i+1]
        right_right=buildings[i]-buildings[i+2]

        #왼쪽 left_cnt만큼 확보 ->오른쪽도 고려해서 cnt++
        if right<=0 or right_right<=0:
            continue
        else:
        # 오른쪽 조망권도 살아있다.->둘 중 작은 것.
            right_cnt = right if right <= right_right else right_right
            cnt += right_cnt if right_cnt<=left_cnt else left_cnt

    print('#'+str(test_case),end=' ')
    print(cnt)
