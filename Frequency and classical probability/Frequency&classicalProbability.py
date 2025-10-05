import random
import matplotlib.pyplot as plt

N = 1_000_000
check = [100, 500, 1000, 5000, 10_000, 50_000,
               100_000, 200_000, 500_000, 1_000_000]

red = 18 / 37
black = 18 / 37
green = 1 / 37

# Теоретическая вероятность: 3 варианта (R,R,B), (R,B,R), (B,R,R)
probability = 3 * (red ** 2) * black
print(f"Теоретическая вероятность: {probability:.6f}")

success_count = 0
results = []  # будем сохранять накопленную частоту на контрольных точках
print()
print("N\t\t\tЧастота")
print("-" * 25)

for trial in range(1, N + 1):
    # Один спин — три раза крутим рулетку
    spins = []
    for _ in range(3):
        r = random.random()
        if r < red:
            spins.append("red")
        elif r < red + black:
            spins.append("black")
        else:
            spins.append("green")

    n_red = spins.count("red")
    n_black = spins.count("black")
    if n_red == 2 and n_black == 1:
        success_count += 1

    if trial in check:
        freq = success_count / trial
        results.append((trial, freq))
        print(f"{trial:_}\t\t{freq:.6f}")

#  График 
Ns, freqs = zip(*results)  

plt.figure(figsize=(12, 7))
plt.plot(Ns, freqs, 'o-', color='darkblue', linewidth=2.5,
         markersize=6, label='Экспериментальная частота', alpha=0.9)
plt.axhline(P_theoretical, color='crimson', linestyle='--', linewidth=3,
            label=f'Теория: {probability:.6f}')

plt.xscale('log')
plt.xlabel('Число испытаний $N$', fontsize=13)
plt.ylabel('Частота события', fontsize=13)
plt.title('Сходимость частоты к теории\n'
          '(ровно 2 красных и 1 чёрный за 3 спина)', fontsize=14)
plt.grid(True, which="both", alpha=0.5, linestyle='--')
plt.legend(fontsize=11)
plt.xticks(ticks=sorted(check),
           labels=[f"{n:,}".replace(",", " ") for n in sorted(check)],
           rotation=0, fontsize=10)
plt.yticks(fontsize=10)
plt.tight_layout()
plt.show()
