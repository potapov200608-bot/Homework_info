import numpy as np
import random
def MNK(x, y) -> list:
    x_val = np.array(x)
    y_val = np.array(y)
    return list(np.polyfit(x_val, y_val, 1))

N = int(input())
x = list((random.uniform(-10000000, 10000000) for i in range(N)))
y = list((random.uniform(-10000000, 10000000) for i in range(N)))

print(*MNK(x, y))
print(*x)
print(*y)