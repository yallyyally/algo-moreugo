#03. 프로그램의 구조를 쌓는다!제어문
######################### 03-1. if문 #########################

money=2000
card=True

if money>=1500 or card:
    #|| 말고 or!
    print('택시타긔')
else:
    print('걸어가긔')

#다중 if문
x=93
if x>=90:
    print('A')
elif x>=80:
    print('B')
elif x>=70:
    print('C')
else:
    print('F')