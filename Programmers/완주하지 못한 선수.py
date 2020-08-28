participant  = ["mislav", "stanko", "mislav", "ana"]
completion= ["stanko", "ana", "mislav"]
answer = ''

dic = {}

# dic[완주자명] = 완주 수
for c in completion:
    if dic.get(c) is not None:
        dic[c] += 1
    else:
        dic[c] = 1

#참가자 명단으로 비교 ->완주자 명단에 없거나 한명 모자라면 out
for p in participant:
    if dic.get(p) is None:
        answer=p
        break
    else:
        dic[p]-=1
else:
    for p in dic:
        if dic[p]<0:
            answer=p
            break
print(answer)
# return answer
