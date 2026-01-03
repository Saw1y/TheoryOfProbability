import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import hypergeom

[N, M, n] = [12, 5, 4]

X = np.arange(0, n + 1)

# Создаём объект гипергеометрического распределения
geom_dist = hypergeom(M=N, n=M, N=n)  # M — общее, n — успехи, N — выборка

# Вероятности
probabilities = geom_dist.pmf(X)

# Характеристики
mean = geom_dist.mean()
var = geom_dist.var()
std = geom_dist.std()

# Мода — автоматически, как вы делали
max_prob = probabilities.max()
mode = X[np.isclose(probabilities, max_prob)]

print(f"Мат. ожидание = {mean:.4f}")
print(f"Дисперсия = {var:.4f}")
print(f"Среднее  ква. отклонение = {std:.4f}")
print(f"Мода = {mode.tolist()}")

# График — многоугольник распределения
plt.figure(figsize=(9, 5))
plt.plot(X, probabilities, 'o-', linewidth=2, markersize=8, color='crimson', label='P(W = k)')
plt.bar(X, probabilities, alpha=0.3, color='lightpink', edgecolor='black')

plt.title('Гипергеометрическое распределение\nЧисло "счастливых" пряников с золотой глазурью', fontsize=12)
plt.xlabel('Число золотых пряников, k')
plt.ylabel('Вероятность P(W = k)')
plt.xticks(X)
plt.grid(True, alpha=0.3)
plt.legend()
plt.show()
