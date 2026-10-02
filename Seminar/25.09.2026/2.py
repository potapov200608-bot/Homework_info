import numpy as np
import matplotlib.pyplot as plt
import random

data_1 = np.random.normal(loc=0, scale=1, size=10)
data_2 = np.random.normal(loc=0, scale=1, size=100)
data_3 = np.random.normal(loc=0, scale=1, size=1000)
data_4 = np.random.normal(loc=0, scale=1, size=10000)
data_5 = np.random.normal(loc=0, scale=1, size=100000)
data_6 = np.random.normal(loc=0, scale=1, size=1000000)

fig, ax = plt.subplots(nrows=2, ncols=3, figsize=(16, 8))

ax1 = ax[0, 0]
ax2 = ax[0, 1]
ax3 = ax[0, 2]
ax4 = ax[1, 0]
ax5 = ax[1, 1]
ax6 = ax[1, 2]

ax1.set_title("Нрормальное распределение 10")
ax2.set_title("Нрормальное распределение 100")
ax3.set_title("Нрормальное распределение 1000")
ax4.set_title("Нрормальное распределение 10000")
ax5.set_title("Нрормальное распределение 100000")
ax6.set_title("Нрормальное распределение 1000000")

ax1.hist(data_1, bins=100, density=True)
ax2.hist(data_2, bins=100, density=True)
ax3.hist(data_3, bins=100, density=True)
ax4.hist(data_4, bins=1000, density=True)
ax5.hist(data_5, bins=1000, density=True)
ax6.hist(data_6, bins=1000, density=True)



plt.show()