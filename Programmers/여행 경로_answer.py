#dfs. 알파벳 순 방문이므로 사전에 key를 공항 이름, 방문 가능 공항을 리스트로 놓고 역순 소팅 (pop 쓰려고)
#막히면 pop.하고 pop한것의 역순 출력
def solution(tickets):
routes = {}
for t in tickets:
    routes[t[0]] = routes.get(t[0],[]) + [t[1]] #리스트 병합

for r in routes: 
    #r은 routes 에 속한 키들임
    routes[r].sort(reverse = True)

stack = ["ICN"] #출발지
path = [] #기록용

#표 개수 만큼..-> 복잡도는 선형적이다.
while len(stack)>0:
    #스택이 다 빌 떄 까지
    
    top = stack[-1]

    #여행 경로에 없으면 -> 갈 곳이 더 이상 없으면
    ##티켓을 다 써버림(키는 있는데 리스트가 빔) or 여기서 출발 하는 게 애초에 한 장도 없음.(키로도 존재 x)
    if len(routes[top])==0 or top not in routes:
        path.append(stack.pop())

    #갈 곳 없으면 pop()-> path에 기록.
    else:
        stack.append(routes[top][-1])
        ##표 없애기
        routes[top] = routes[top][:-1]

return path[::-1]

#stack push, pop -> N
#소팅하는 거 
#표 조사 - 소팅 되었을 시 POP, 일일이 찾아봐야 할 시 N^2