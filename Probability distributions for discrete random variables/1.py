import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom

# Параметры
n = 6
p = 0.1

# Создаём объект биномиального распределения
binomial_dist = binom(n, p)

# Значения X: от 0 до n
X = np.arange(0, n + 1)

# Вероятности P(X=k)
probabilities = binomial_dist.pmf(X)

# Математическое ожидание, дисперсия, СКО
mean = binomial_dist.mean()
variance = binomial_dist.var()
std_dev = binomial_dist.std()

print(f"Мат. ожидание = {mean:.5f}")
print(f"Дисперсия = {variance:.5f}")
print(f"Ст. отклонение = {std_dev:.5f}")

# Мода
max_prob = probabilities.max()
mode = [int(x) for x in X if round(probabilities[int(x)], 6) == round(max_prob, 6)]
print(f"Мода = {mode}")

# Построение многоугольника распределения
plt.figure(figsize=(9, 5))
plt.plot(X, probabilities, 'o-', linewidth=2, markersize=8, color='darkblue', label='Многоугольник')
plt.bar(X, probabilities, alpha=0.3, color='lightblue', edgecolor='black', label='Гистограмма')

plt.title(f'Биномиальное распределение (n={n}, p={p})\nЧисло отказавших деталей, m', fontsize=12)
plt.xlabel('Число отказавших деталей, m')
plt.ylabel('Вероятность P(X=m)')
plt.xticks(X)
plt.grid(True, alpha=0.3)
plt.legend()
plt.show()
