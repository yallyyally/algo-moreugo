import sys

#sys.stdin = open("in3.txt","rt")
#���� �˰������� Ǯ �� �ִ� ���� -> ���� ������ �ٷ� �� �� �ִ�.
##���� ���� Ư�� ���ڸ� ���س��� ��ȿ�ϳ�, �ƴϳĸ� Ȯ���Լ��� Ȯ����.-> ������ ������..

# ���� �� ���� ���̴� 1~ ���� ū ������ ���� (802) ����.-> �� ���� ������ �̺�Ž���� �õ��Ѵ�.

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
            #�ӽ�������...
            res = temp_length
            #k���� ũ�ϱ� �� ū ũ��� ������ �� -> k�� ���ų� (����) ������ ũ���� ���̴� ������ �� Ŀ��
            #res �� ���� �ʿ� X
            binarySearch(temp_length+1,end)
        elif temp==k:
            print(temp_length)
        else :
            #k���� �����ϱ� �� ���� ũ��� ������ ��
            binarySearch(start,temp_length-1)

            #�� ���� k���� ū �������� �ּ���
N,k = map(int,sys.stdin.readline().split())

#N���� ���� k���� �յ��ϰ� �����

for _ in range(N):
    cables.append(int(sys.stdin.readline()))
cables.sort(reverse = True)

#1~max ������ ��
max = cables[0]
binarySearch(1,max)

