
N = int(input())
s = list((input().split()))
a = 0
b = 0
for c in s:
    a = 0
    b = 0
    for v in s:
        if c < v:
            a = a + 1
        elif c > v:
            b = b + 1
    if a == b:
        print(c)
        break
    
