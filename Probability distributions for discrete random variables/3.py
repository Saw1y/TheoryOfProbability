import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import geom
import pandas as pd
# Параметр распределения
p = 0.2

# Создаём распределение
geom_dist = geom(p)

# Возможные значения Z: от 1 до 20 (дальше вероятности очень малы)
z_vals = np.arange(1, 21)
probs = geom_dist.pmf(z_vals)

pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
k = 14
df = pd.DataFrame(data=probs[:k + 1].reshape(1, -1),
                  columns=z_vals[:k + 1],
                  index=['p'])
print(df)
# Характеристики
mean = geom_dist.mean()
var = geom_dist.var()
std = geom_dist.std()

max_prob = probs.max()
mode_vals = z_vals[np.isclose(probs, max_prob)]

print(f"Математическое ожидание: {mean:.5f}")
print(f"Дисперсия: {var:.5f}")
print(f"Среднее квадратичное отклонение: {std:.5f}")
print(f"Мода: {mode_vals.tolist()}")

# Многоугольник распределения
plt.figure(figsize=(9, 5))
plt.plot(z_vals, probs, 'o-', linewidth=2, markersize=8, color='darkorange', label='P(Z = k)')
plt.bar(z_vals, probs, alpha=0.3, color='peachpuff', edgecolor='black')

plt.title('Геометрическое распределение (p = 0.2)\nНомер первой удачной попытки с мандаринами', fontsize=12)
plt.xlabel('Номер попытки, k')
plt.ylabel('Вероятность')
plt.xticks(z_vals[::2])
plt.grid(True, alpha=0.3)
plt.legend()
plt.show()
