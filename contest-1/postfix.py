postfix = input().rstrip()
postfix = postfix.split(' ')
ops = {
    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y,
    '*': lambda x, y: x * y,
    '/': lambda x, y: x / y
}

res = []
for p in postfix:
    if p in ops:
        b, a = res.pop(), res.pop()
        op = ops[p]
        res.append(op(a, b))
    else:
        res.append(int(p))

print(res[-1])
