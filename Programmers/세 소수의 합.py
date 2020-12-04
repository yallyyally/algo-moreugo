# -*- coding:utf-8 -*-
answer = 0
def check(n):
    #체 완성해서 소수 배열 return
    prime = []
    sieve = [1]*(n+1)
    
    ##0, 1은 소수가 아님 (n은 자연수)
    sieve[0],sieve[1] = 0, 0
    
    #2. 에라토스테네스의 체
    for i in range(2,n):
        #해당 수가 소수일때만 그 배수를 처낸다
        if sieve[i]:
            j=2
            while i*j<=n:
                sieve[i*j] = 0
                j+=1
    
    #걸러진 소수들 모음
    for i in range(2,n):
        if sieve[i]:
            prime.append(i)
    
    return prime

def solution(n):
    prime = []
    selected = []
    breakj_flag = 0
    breaki_flag = 0
    global answer
    #1. n 미만의 소수를 구한다. - 에라토스테네스의 체 이용
    prime = check(n)
    
    #2. prime에서 selected 정하기
    ##prime 개수는 3개 이상이어야함
 
    for i in range(len(prime)):
        selected.clear()
        if prime[i] > n:
            break
        selected.append(prime[i])
        breaki_flag = 0
        for j in range(i+1, len(prime)):
            if sum(selected) + prime[j] < n:
                selected.append(prime[j])
                breakj_flag = 0
                for k in range(j+1, len(prime)):
                    if sum(selected) + prime[k] == n:
                        answer+=1
                        break
                    elif sum(selected) + prime[k]>n:
                        break
                selected.pop()

            else:
                break
        selected.pop()

    
    return answer

n = 33
print(solution(n))