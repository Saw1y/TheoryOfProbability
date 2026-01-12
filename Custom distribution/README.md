# Анализ собственного распределения $\frac{4 \cos^2{x}}{\pi}$ с применением методов теории вероятностей

## О распределении

Собственное **непрерывное распределение** определено на интервале **[0, $\frac{π}{2}$]** с плотностью вероятности **$\phi(x) = \frac{4 \cos^2{x}}{\pi}$**.  
Наследуется от `scipy.stats.rv_continuous` и реализовано в классе `CustomDistribution`.  
**Параметры**: `a = 0`, `b = π/2 `.

### Формулы распределения

**Плотность вероятности (PDF)**:


$$
\phi(x) = \begin{cases} 
\frac{4 \cos^2{x}}{\pi}, & x \in [0, \frac{\pi}{2}] \\
0, & \text{иначе}
\end{cases}
$$

**Функция распределения (CDF)**:

$$
F(x) = \begin{cases} 
0, & x \le 0 \\
\frac{2x + \sin{2x}}{\pi}, & 0 < x \le \frac{\pi}{2} \\
1, & x > \frac{\pi}{2}
\end{cases}
$$

---

Для данной функции требуется:
* проверить условие нормировки плотности;
* построить графики плотности и функции распределения;
* рассчитать вероятность попадания случайной величины в некоторый интервал;
* вычислить математическое ожидание, дисперсию и среднее квадратическое отклонение; 
* вычислить квантиль уровня q и p%-ную точку случайной величины;
* определить коэффициент асимметрии и эксцесс.
![Решение](https://github.com/Saw1y/TheoryOfProbability/blob/main/Custom%20distribution/custom.ipynb)
## 1. Нормировка плотности
![](https://github.com/Saw1y/TheoryOfProbability/blob/main/Custom%20distribution/custom1.png)
## 2. Графики плотности и функции распределения 
![](https://github.com/Saw1y/TheoryOfProbability/blob/main/Custom%20distribution/custom2.png)
## 3. Вероятноть попадания св в некоторый интревал
![](https://github.com/Saw1y/TheoryOfProbability/blob/main/Custom%20distribution/custom3.png)
## 4. Вычислить мат. ожидание, дисперсию, ско
![](https://github.com/Saw1y/TheoryOfProbability/blob/main/Custom%20distribution/custom4.png)
## 5. Вычислить квантиль уровня q и p%-ную точку случайной величины
![](https://github.com/Saw1y/TheoryOfProbability/blob/main/Custom%20distribution/custom5.png)
## 6. Определить коэффициент асимметрии и эксцесс
![](https://github.com/Saw1y/TheoryOfProbability/blob/main/Custom%20distribution/custom6.png)
