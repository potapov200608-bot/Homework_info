
import random
import matplotlib.pyplot as plt

N = 100 ##int(input())
x = list((random.uniform(-100, 100) for i in range(N)))
y = list((random.uniform(-100, 100) for i in range(N)))

plt.figure(figsize=(10, 10))
plt.scatter(x, y, marker = 'x' )
plt.title('распределение значений х по у')#Пример использования такой диаграммы - например, точки падения шарика с высоты)
plt.xticks([i for i in range(int(min(x))-2, int(max(x))+2, 2)], minor = True)
plt.yticks([i for i in range(int(min(y))-2, int(max(y))+2, 2)], minor = True)
plt.xlabel('Координата X')
plt.ylabel('координата Y')
plt.grid()
plt.show()