class MyQueue:
    def __init__(self):
        self.queue = [[], []]

    def push(self, n):
        self.queue[0].append(n)
        print('ok')

    def pop(self):
        if len(self.queue[1]) == 0:
            self.queue[1] = self.queue[0][::-1]
            self.queue[0] = []
        print(self.queue[1][-1])
        self.queue[1].pop()

    def front(self):
        if len(self.queue[1]) == 0:
            self.queue[1] = list(reversed(self.queue[0]))
            self.queue[0] = []
        print(self.queue[1][-1])

    def size(self):
        print(len(self.queue[0]) + len(self.queue[1]))

    def clear(self):
        self.queue = [[], []]
        print('ok')


q = MyQueue()
command = list()
c = ''

while c != 'exit':
    c = input()
    command.append(c)

for cmd in command:
    if 'push' in cmd:
        cmd = cmd.split(' ')
        q.push(int(cmd[1]))
    if cmd == 'pop':
        q.pop()
    if cmd == 'front':
        q.front()
    if cmd == 'size':
        q.size()
    if cmd == 'clear':
        q.clear()
    if cmd == 'exit':
        print('bye')
