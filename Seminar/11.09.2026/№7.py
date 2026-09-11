s = list(input().split())
d = 0
for a in s:
    c = 0
    for b in s:
        if a == b:
            c += 1
    if c > d:
        d = c
        z = a
print(z)