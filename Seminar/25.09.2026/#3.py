import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('iris_data.csv')

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

species_counts = df['Species'].value_counts()
ax1.pie(
    species_counts, 
    labels=species_counts.index, 
    autopct='%1.1f%%', 
    startangle=140, 
    colors=['red', 'blue', 'green']
)
ax1.set_title('Доля разных видов ирисов (Species)', fontsize=12, fontweight='bold')

c1 = df[df['PetalLengthCm'] < 1.2].shape[0]
c2 = df[(df['PetalLengthCm'] >= 1.2) & (df['PetalLengthCm'] <= 1.5)].shape[0]
c3 = df[df['PetalLengthCm'] > 1.5].shape[0]

lengths = [c1, c2, c3]
labels = ['Меньше 1.2 см', 'От 1.2 см до 1.5 см\n(включительно)', 'Больше 1.5 см']

ax2.pie(
    lengths, 
    labels=labels, 
    autopct='%1.1f%%', 
    startangle=140, 
    colors=['#ffcc99', '#c2c2f0', '#b3e6b3']
)
ax2.set_title('Доли ирисов по длине лепестка (PetalLengthCm)', fontsize=12, fontweight='bold')

plt.tight_layout()
plt.show()
