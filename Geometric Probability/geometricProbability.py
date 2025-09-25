import numpy as np
import matplotlib.pyplot as plt

wall_w = 2.0         
wall_h = 2.0        
target_w = 1.0      
target_h = 0.5      

target_left = wall_w - target_w   
target_bottom = 0.0               

num_shots = 300_000   # количество бросков

# Генерация случайных точек
x_points = np.random.uniform(0, wall_w, num_shots)
y_points = np.random.uniform(0, wall_h, num_shots)


x_hits = []     
y_hits = []
x_misses = []   
y_misses = []

for i in range(num_shots):
    x = x_points[i]
    y = y_points[i]
    
    if x >= target_left and x <= wall_w and y >= target_bottom and y <= target_bottom + target_h:
        x_hits.append(x)
        y_hits.append(y)
    else:
        x_misses.append(x)
        y_misses.append(y)

num_hits = len(x_hits)

total_area = wall_w * wall_h
target_area = target_w * target_h
prob_empirical = num_hits / num_shots

print(f"Количество бросков: {num_shots}")
print(f"Количество попаданий: {num_hits}")
print(f"Геометрическая вероятность: {prob_empirical:.4f}")

#  График 
plt.figure(figsize=(6, 6))

# Рамка всей зоны
plt.plot([0, wall_w, wall_w, 0, 0], [0, 0, wall_h, wall_h, 0],
         color='black', linewidth=2, label="Общая зона (2×2 м)")

# Целевая зона — справа снизу
plt.fill([target_left, wall_w, wall_w, target_left],
         [target_bottom, target_bottom, target_bottom + target_h, target_bottom + target_h],
         color='green', alpha=0.3, label="Целевая зона (1×0.5 м)")

# Отрисовываем все точки сразу 
plt.scatter(x_misses, y_misses, c='red', s=2, alpha=0.6, label='Промахи')
plt.scatter(x_hits, y_hits, c='lime', s=5, edgecolors='darkgreen', label='Попадания')

# Оформление
plt.xlim(0, wall_w)
plt.ylim(0, wall_h)
plt.xlabel("Ширина (м)")
plt.ylabel("Глубина (м)")
plt.title("Моделирование геометрической вероятности")
plt.legend()
plt.grid(True, alpha=0.3)
plt.gca().set_aspect('equal', adjustable='box')  
plt.tight_layout()

# Показать график
plt.show()
