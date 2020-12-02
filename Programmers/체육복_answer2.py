#그리디
def solution(n,lost,reserve):
    #set 사용 -hash로 구현
    #value가 아니라, 집합에 속했는지 아닌지만 알려줌
    #숨겨짐 (len(lost),len(reserved))
    s = set(lost) & set(reserve) #가져왔으나 도난당함 -> reserved에서 제외
    l = set(lost) - s #진정 잃어버린 자들
    r = set(reserve) - s
    #KlogK + K
    for x in sorted(r):
        if x-1 in l:
            l.remove(x-1)
        elif x+1 in l:
            l.remove(x+1)

    return n - len(l)

##전체 - KlogK