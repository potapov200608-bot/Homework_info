s = list((input().split()))
s[::2], s[1::2] = s[1::2], s[::2]

print(*s)