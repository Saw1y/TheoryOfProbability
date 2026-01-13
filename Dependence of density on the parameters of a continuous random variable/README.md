# Распределение Стьюдента

*Определение* **Распределением Стьюдента** (или t-распределением) называется распределение случайной велечины

$$ t = \frac{Z}{\sqrt{\frac{1}{k} χ^2}}$$

, где Z - случайная величина, распределённая по стандартному закону, т.e. N(0;1)

χ^2 - независимая от Z случайная величина, имеющая χ^2 - распределение с k степенем свободы

---

**Плотность вероятности распределения Стьюдента** имеет следующий вид:

$$φ(x) = \frac{Г(\frac{k + 1}{2})}{Г(\frac{k}{2}) \sqrt{\pi k}} (1 + \frac{x^2}{n})^{-\frac{k + 1}{2}}$$

---
При k → ∞ t-распределение приближается к нормальному. Практически уже при  k > 30 можно считать t-распредление приближено к нормальному.

---
**Числовые характеристики**
* Математическое ожидание: $M(t) = 0$
* Дисперсия: $D(t) = \frac{k}{k-2}$
![Решение](https://github.com/Saw1y/TheoryOfProbability/blob/main/Dependence%20of%20density%20on%20the%20parameters%20of%20a%20continuous%20random%20variable/Dependence%20of%20density.ipynb) 
![](https://github.com/Saw1y/TheoryOfProbability/blob/main/Dependence%20of%20density%20on%20the%20parameters%20of%20a%20continuous%20random%20variable/density1.png )
