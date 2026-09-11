N = int(input())
s = input()
d = []
for i in range(0, len(s), N):
    d.extend(s[i:i+N][::-1])
print(*d)