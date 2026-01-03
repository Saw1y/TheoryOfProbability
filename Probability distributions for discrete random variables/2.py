import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import poisson
import pandas as pd
# Параметр распределения
lam = 2.5

# Создаём распределение
pois = poisson(mu=lam)

# Диапазон значений Y (берём до 20 — дальше вероятности пренебрежимо малы)
y_vals = np.arange(0, 21)
probs = pois.pmf(y_vals)

pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
k = 13
df = pd.DataFrame(data=probs[:k + 1].reshape(1, -1),
                  columns=y_vals[:k + 1],
                  index=['p'])
print(df)
# Вывод характеристик
print(f"Мат.ожидание: {pois.mean():.5f}")
print(f"Дисперсия: {pois.var():.5f}")
print(f"Среднее квадратическое отклонение: {pois.std():.5f}")

# Мода 
max_prob = probs.max()
mode_vals = y_vals[np.isclose(probs, max_prob)]
print(f"Мода: {mode_vals.tolist()}")


# Построение многоугольника распределения
plt.figure(figsize=(9, 5))
plt.plot(y_vals, probs, 'o-', linewidth=2, markersize=8, color='darkgreen', label='Многоугольник')
plt.bar(y_vals, probs, alpha=0.3, color='lightgreen', edgecolor='black', label='Вероятности')

plt.title(f'Распределение Пуассона (λ = {lam})\nЧисло новорождённых креветок за сутки', fontsize=12)
plt.xlabel('Число креветок, k')
plt.ylabel('Вероятность P(Y = k)')
plt.xticks(y_vals)
plt.grid(True, alpha=0.3)
plt.legend()
plt.show()
