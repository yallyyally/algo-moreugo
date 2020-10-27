#N개의 정수 A[1], A[2], ..., A[N]이 주어져 있을 때,
#이 안에 X라는 정수가 존재하는지 알아내는 프로그램을
#작성하시오.
import sys

def search(list,x,start,end):
    if start>end:
        print('0') #return 0 하면 main 함수가 아니고 본인함수로 돌아온다.유의할 것
        return
    else:
        mid = (start+end)//2
        if x==list[mid]:
            print('1')
            return
        elif x>list[mid]:
            search(list,x,mid+1,end)
        elif x<list[mid]: #x<mid
            search(list,x,start,mid-1)

N = int(sys.stdin.readline())
numbers = sorted(list(map(int,sys.stdin.readline().split())))
M = int(sys.stdin.readline())
finding = list(map(int,sys.stdin.readline().split()))
#finding 속의 숫자들이 numbers에 포함되면 1, 존재 하지 않으면 0

for x in finding:
    search(numbers,x,0,N-1)
