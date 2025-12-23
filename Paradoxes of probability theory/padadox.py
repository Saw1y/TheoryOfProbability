import random
import matplotlib.pyplot as plt

# Модель игры: бросаем монету до первого орла
# Выигрыш = 2^k, где k — номер броска, на котором выпал орёл
def play():
    k = 1
    while random.random() < 0.5:  # решка — продолжаем
        k += 1
        if k > 30:  # на всякий случай ограничим, хотя шанс ничтожен
            break
    return 2 ** k

# Запускаем n игр
# max_payout — чтобы не сломать банк, если вдруг кто-то выиграет миллиард
def simulate(n, max_payout=None):
    wins = []
    for _ in range(n):
        win = play()
        if max_payout and win > max_payout:
            win = max_payout  # обрезаем по лимиту
        wins.append(win)
    return wins


# --- Настройки ---
num_games = 1_000_000      # много игр, чтобы среднее стабилизировалось
max_payout = 1_048_576     # примерно миллион — 2^20, дальше не платим больше

print("Запускаю симуляцию...")
results = simulate(num_games, max_payout)

# Считаем среднее и медиану
avg = sum(results) / len(results)
med = sorted(results)[len(results)//2]

print(f"Средний выигрыш: {avg:.2f} руб")
print(f"Медианный: {med} руб (почти все получают 2 или 4)")


running_avg = []
total = 0
for i, win in enumerate(results):
    total += win
    running_avg.append(total / (i + 1))

plt.figure(figsize=(10, 5))
plt.plot(running_avg, color='green', linewidth=1.2, alpha=0.8)
plt.axhline(avg, color='red', alpha=0.7, linestyle='-')
plt.title('Динамика среднего выигрыша')
plt.xlabel('Число проведённых игр')
plt.ylabel('Текущее среднее')
plt.ylim(0, avg * 1.5)
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()


# --- Сколько можно брать за вход? ---
print("\n--- Оценка цены входа ---")
prices = [20, 30, 50, 100]
for p in prices:
    profit_per = p - avg
    total_profit = profit_per * num_games
    status = "прибыль" if profit_per > 0 else "убыток"
    print(f"{p:3}₽: {profit_per:6.1f}₽/игру → {status} ({int(total_profit):>+12,}₽)")

print(f"\nВывод: если брать от {int(avg)+10}₽ — уже в плюсе.")
