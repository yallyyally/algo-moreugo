# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean

def countExercise(p,max):
    x = p/max *100
    if x >= 90:
        exercise[0]+=1
    elif x>=80:
        exercise[1]+=1
    elif x >= 75:
        exercise[2]+=1
    elif x >= 68:
        exercise[3]+=1
    elif x >= 60:
        exercise[4]+=1
    else:
        exercise[5]+=1


#운동 형태
exercise=[0]*6
#나이
N = int(input())
#최대 심박수
maxpulse = 220-N

#공백일때까지 입력?
while True:
    try:
        p=int(input())
        countExercise(p,maxpulse)
    except EOFError:
        break
for x in exercise:
    print(x,end=' ')

def countExercise(p,max):
    x = p/max *100
    if x >= 90:
        exercise[0]+=1
    elif x>=80:
        exercise[1]+=1
    elif x >= 75:
        exercise[2]+=1
    elif x >= 68:
        exercise[3]+=1
    elif x >= 60:
        exercise[4]+=1
    else:
        exercise[5]+=1


#운동 형태
exercise=[0]*6
#나이
N = int(input())
#최대 심박수
maxpulse = 220-N

#공백일때까지 입력?
while True:
    try:
        p=int(input())
        countExercise(p,maxpulse)
    except EOFError:
        break
for x in exercise:
    print(x,end=' ')
