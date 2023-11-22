# Обчислення інтеграла методом Сімпсона
from scipy import integrate
import numpy as np


# Задаємо функцію, яку необхідно інтегрувати
def f2(x):
    return np.log10(x**2 + 1) / (x + 1)


# Задаємо межі інтегрування та початкову кількість розбиттів
a = 0.8
b = 1.6
n = 8


# Обчислюємо значення інтегралу методом Сімпсона
def simpson_rule(f2, a, b, n):
    h = (b - a) / n
    integr = f2(a) + f2(b)
    for i in range(1, n):
        k = a + i * h
        if i % 2 == 0:
            integr += 2 * f2(k)
        else:
            integr += 4 * f2(k)
    integr *= h / 3
    return integr


# Обчислюємо значення інтегралу методом Сімпсона з точністю 0.001
integral1 = simpson_rule(f2, a, b, n)
n *= 2
integral2 = simpson_rule(f2, a, b, n)
while abs(integral2 - integral1) / 15 > 0.001:
    integral1 = integral2
    n *= 2
    integral2 = simpson_rule(f2, a, b, n)

# Виводимо результат
print("Simpsone method:", round(integral2, 5))

v, err = integrate.quad(f2, a, b)  # Перевірка
print("Check for the Simpsone method= ", round(v, 5))
