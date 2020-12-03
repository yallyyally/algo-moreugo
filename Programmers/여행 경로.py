#dfs. 알파벳 순 방문이므로 사전에 key를 공항 이름, 방문 가능 공항을 리스트로 놓고 역순 소팅 (pop 쓰려고)
#막히면 pop.하고 pop한것의 역순 출력
def solution(tickets):
routes = {}
for t in tickets:
    routes[t[0]] = routes.get(t[0],[]) [t[1]] #리스트 병합

for r in routes: 
    #r은 routes 에 속한 키들임
    routes[r].sort(reverse = True)

stack = ["ICN"] #출발지
path = [] #기록용

while len(stack)>0:
    #스택이 다 빌 떄 까지
    
    top = stack[-1]

    #갈 곳 있으면 방문 (push)
    if len(routes[top])>0:
        stack.append(routes[top].pop())

    #갈 곳 없으면 pop()-> path에 기록.
    else:
        path.append(stack.pop())
