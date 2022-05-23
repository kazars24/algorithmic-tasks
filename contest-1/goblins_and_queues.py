from collections import deque


class Queue:
    def __init__(self):
        self.l = deque()
        self.r = deque()

    def push(self, v: int):
        self.l.appendleft(v)
        #print(self.l, self.r)

    def push_mid(self, v: int):
        while len(self.l) > len(self.r):
            self.r.appendleft(self.l.pop())
        self.l.append(v)
        #print(self.l, self.r)

    def pop(self) -> int:
        while len(self.l) > len(self.r):
            self.r.appendleft(self.l.pop())
        #print(self.l, self.r)
        return self.r.pop()


q = Queue()
n = int(input())
for _ in range(n):
    cmd = input().split()
    if cmd[0] == '+':
        q.push(int(cmd[1]))
    if cmd[0] == '*':
        q.push_mid(int(cmd[1]))
    if cmd[0] == '-':
        print(q.pop())
