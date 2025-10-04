import numpy as np
import matplotlib.pyplot as plt

num_simulations = 1_000_000  # Число троек опытов
check_points = np.array([
    100, 500, 1000, 5000, 10_000, 50_000,
    100_000, 200_000, 500_000, 1_000_000
])

# Рулетка: 0=red, 1=black, 2=green 
colors = np.array(['red', 'black', 'green'])
probs = [18/37, 18/37, 1/37]  # Вероятности цветов

P_theoretical = 3 * (18/37)**2 * (18/37)
print(f"Теоретическая вероятность: {P_theoretical:.6f}")


spins_indices = np.random.choice([0, 1, 2], size=(num_simulations, 3), p=probs)

red_count = np.sum(spins_indices == 0, axis=1)  # Сколько 'red' в каждом из 3 спинов
black_count = np.sum(spins_indices == 1, axis=1)  # Сколько 'black'

# Определяем успех: ровно 2 красных и 1 чёрный
success = (red_count == 2) & (black_count == 1)  

# Накопленная частота в контрольных точках
cumulative_success = np.cumsum(success)  # Количество успехов к каждому шагу
N_list = []
freq_list = []

print("\nN\t\t\tЧастота")
print("-" * 25)

for N in check_points:
    if N <= num_simulations:
        freq = cumulative_success[N - 1] / N  # Частота после N опытов
        N_list.append(N)
        freq_list.append(freq)
        n_formatted = f"{N:_}".replace("_", " ")
        print(f"{n_formatted}\t\t{freq:.6f}")

# === Построение графика ===
plt.figure(figsize=(14, 8))
plt.plot(N_list, freq_list, 'o-', color='mediumblue', linewidth=2.5, markersize=6,
         label='Частота события', alpha=0.9)
plt.axhline(y=P_theoretical, color='crimson', linestyle='--', linewidth=3,
            label=f'Теоретическая вероятность ({P_theoretical:.6f})')

plt.xscale('log')
plt.xlabel('Число испытаний $N$', fontsize=14)
plt.ylabel('Частота события', fontsize=14)
plt.title('Сходимость частотной вероятности к теоретической\n'
          '(Ровно 2 красных и 1 чёрный за 3 спина)',
          fontsize=16, pad=20)
plt.grid(True, which="both", linestyle='--', alpha=0.6)
plt.legend(fontsize=12)
plt.xticks(ticks=check_points, labels=[f"{int(n):,}".replace(",", " ") for n in check_points],
           rotation=0, fontsize=11)
plt.yticks(fontsize=11)
plt.tight_layout()

# Показать график
plt.show()
