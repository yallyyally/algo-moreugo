# -*- coding:utf-8 -*-

import sys

class MyStack(object):
    def __init__(self):
        self.lst = list()

    def push(self, x):
        self.lst.append(x)

    def pop(self):
        return self.lst.pop()

    def size(self):
        return len(self.lst)

class MyQueue(object):
    def __init__(self, max_size):
        self.stack1 = MyStack()
        self.stack2 = MyStack()
        self.max_size = max_size

    def qsize(self):
        return self.stack1.size()

    def push(self, item):
        if self.qsize()==self.max_size:
            return 'False'
       
        else:#######stack에 하나도 없을 때
            #하나도 없으면 걍 push
            if self.qsize()==0:
                self.stack1.push(item)
                
            else:
                #1. 지금 있는 걸 거꾸로 만듦 -> 늦게 들어온 거위에 놓으려고
                for i in range(self.stack1.size()):
                    self.stack2.push(self.stack1.pop())
                #그 위에 올려놓기
                self.stack2.push(item)
                #그거 거꾸로 해서 stack1 만들기
                for i in range(self.stack2.size()):
                    self.stack1.push(self.stack2.pop())
                #stack2 초기화
                self.stack2 = MyStack()
            print(self.stack1.lst)
            return 'True'

    def pop(self):
        if self.qsize()>0:
            return str(self.stack1.pop())
        elif self.qsize()==0:
            return 'False'
        
    
n, max_size = map(int, input().strip().split(' '))
queue = MyQueue(max_size)
answer = ''

for c in range(n):
    cmd = sys.stdin.readline()
    #중간에 공백이 있을 경우
    #맨뒤 두글자 자르기
    cmd = cmd[:-1]
    if ' ' in cmd:
        #공백 처리
        command, arg = cmd.split(' ')
    #중간에 공백이 없을 경우
    else:
        command = cmd
     #명령어 처리
    if command == 'PUSH':
        print(queue.push(int(arg)))
    
    elif command == 'POP':
        print(queue.pop())

    elif command == 'SIZE':
        print(queue.qsize())


        
