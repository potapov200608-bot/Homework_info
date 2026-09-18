import numpy as np
def MNK(x: list, y: list) -> list:
    x_val = np.array(x)
    y_val = np.array(y)
    return list(np.polyfit(x_val, y_val, 1))

x = list(map(int, input().split()))
y = list(map(int, input().split()))

print(*MNK(x, y))