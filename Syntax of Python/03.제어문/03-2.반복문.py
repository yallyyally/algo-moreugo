#03. 프로그램의 구조를 쌓는다!제어문
######################### 03-2. 반복문 #########################

a = range(1,10) #1~9까지 정수 리스트 만듦
b = range(10) #0~9까지 리스트 만듦
print(list(a)) #a를 list 화
#[1, 2, 3, 4, 5, 6, 7, 8, 9]

#1. for문
for i in range(10):
   # print("hi "+str(i))
    print("hi",end=str(i))
    #나의 예상: hi0\nhi1\n..
    #출력 결과: hi0hi1hi2.. (개행x 이유: end='\n'이 디폴트인데 이걸 바꿔 줌)
#for i in range(10,0)->아무일도 안일어남: +1이 디폴트라서,,
#for i in range(10,0,-1) -> 10~1까지
print('\n')
#1~10에서 홀수만 출력
for i in range(1,11):
    if i%2==0:
        continue
        #밑에꺼 수행 x 하고 i 증가
    print(i)
#if + break
for i in range(1,11):
    print(i)
    if i==7:
        break


#2. while 문

i=1
#while i<=10
while True:
    print(i)
    if i==5:
        break
    i=i+1


