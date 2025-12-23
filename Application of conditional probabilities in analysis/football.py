import pandas as pd

df = pd.read_csv('fifa_players_clean.csv')

# Показать первые строки для проверки
print("Первые 5 строк данных:")
print(df.head())
print("\n" + "="*50)



# 2. АПРИОРНЫЕ ВЕРОЯТНОСТИ
print("2. АПРИОРНЫЕ ВЕРОЯТНОСТИ")
print("-" * 30)

# P(age=30) — игроку ровно 30 лет
P_age_30 = (df['age'] == 30).mean()
print(f"P(age=30) = {P_age_30:.3f}")

# P(foot) — вероятность быть правшой или левшой
for foot in df['preferred_foot'].unique():
    P_foot = (df['preferred_foot'] == foot).mean()
    print(f"P({foot}) = {P_foot:.3f}")

# P(position=ST) — игрок играет на позиции ST
P_ST = df['positions'].str.contains('ST').mean()
print(f"P(position=ST) = {P_ST:.3f}")

print("\n" + "="*50)


# ========================
# 3. P(ST | Right)
# Какова вероятность, что игрок — нападающий, если он правша?
# ========================
print("3. УСЛОВНАЯ ВЕРОЯТНОСТЬ: P(ST | Right)")
print("-" * 30)

# Способ 1: По формуле
right = df[df['preferred_foot'] == 'Right']
p_right = len(right) / len(df)
st_right = right[right['positions'].str.contains('ST')]
p_st_right = len(st_right) / len(df)
p = p_st_right / p_right
print(f"P(ST | Right), вручную: {p:.3f}")

# Способ 2: Через фильтр
p = right['positions'].str.contains('ST').mean()
print(f"P(ST | Right), через фильтр: {p:.3f}")

print("\n" + "="*50)


# ========================
# 4. P(Height>185 | Defender)
# Какова вероятность, что защитник выше 185 см?
# ========================
print("4. УСЛОВНАЯ ВЕРОЯТНОСТЬ: P(Height>185 | Defender)")
print("-" * 30)

# Способ 1: По формуле
defenders = df[df['positions'].str.contains('CB|RB|LB')]
p_def = len(defenders) / len(df)
tall_def = defenders[defenders['height_cm'] > 185]
p_tall_def = len(tall_def) / len(df)
p = p_tall_def / p_def
print(f"P(Height>185 | Defender), вручную: {p:.3f}")

# Способ 2: Через фильтр
p = (defenders['height_cm'] > 185).mean()
print(f"P(Height>185 | Defender), через фильтр: {p:.3f}")

print("\n" + "="*50)


# ========================
# 5. P(Age>30 | Overall>80)
# Какова вероятность, что игрок старше 30, если его рейтинг > 80?
# ========================
print("5. УСЛОВНАЯ ВЕРОЯТНОСТЬ: P(Age>30 | Overall>80)")
print("-" * 30)

# Способ 1: По формуле
high = df[df['overall_rating'] > 80]
p_high = len(high) / len(df)
old_high = high[high['age'] > 30]
p_old_high = len(old_high) / len(df)
p = p_old_high / p_high
print(f"P(Age>30 | Overall>80), вручную: {p:.3f}")

# Способ 2: Через фильтр
p = (high['age'] > 30).mean()
print(f"P(Age>30 | Overall>80), через фильтр: {p:.3f}")
