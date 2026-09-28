def E(a, b):
    if b == 0:
        return a
    return E(b, a % b)

a, b = input().split()
a, b = int(a), int(b)
print(E(a, b))
#Файд временно в ремонте :)
