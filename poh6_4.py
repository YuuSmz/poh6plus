n = int(input())
l = sorted([input() for i in range(n)])
c = []
s = ""
for i in l[:]:
    r = i[::-1]
    if i == r and l.count(i) == 1:
        c.append(i)
    elif r in l:
        s += i
        l.remove(i)
        l.remove(r)
print(s + c[0] + s[::-1] if c else s + s[::-1])
