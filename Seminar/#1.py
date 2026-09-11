a = int(input())
N = []
b = 0
for i in range(a+1):
    b += i
for i in range(a-1):
    N.append(int(input()))
print(b-sum(N))