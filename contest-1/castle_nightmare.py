def itoc(i):
    return chr(ord('a') + i)


s = input()
w = list(map(int, input().split(' ')))

cnt = [0] * 26
for c in s:
    cnt[ord(c) - ord('a')] += 1

chars = list(range(26))
chars.sort(key=lambda x: w[x], reverse=True)

l, r = [], []
for c in chars:
    if cnt[c] > 1:
        l.append(itoc(c))
        r.append(itoc(c))
        cnt[c] -= 2
for c in range(26):
    while cnt[c] != 0:
        l.append(itoc(c))
        cnt[c] -= 1
print(''.join(l + r[::-1]))
