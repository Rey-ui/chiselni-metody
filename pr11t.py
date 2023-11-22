# Обчислення інтеграла методом трапецій
from scipy import integrate
import numpy as np

eps = 0.0001
a = 1.2
b = 2.7
n = 20


def f3(x):
    return 1 / np.sqrt(x**2 + 3.2)


def trapezoidal_rule(f3, a, b, n):
    h = (b - a) / n
    x = a
    sum = 0
    for i in range(1, n):
        x += h
        sum += 2 * f3(x)
    sum += f3(b)
    integral = h / 2 * sum

    return integral


integral1 = trapezoidal_rule(f3, a, b, n)
n *= 2
integral2 = trapezoidal_rule(f3, a, b, n)
while abs(integral2 - integral1) / 3 > 0.001:
    integral1 = integral2
    n *= 2
    integral2 = trapezoidal_rule(f3, a, b, n)

# Виводимо результат
print("Trapetzia methodof:", round(integral2, 5))

v, err = integrate.quad(f3, a, b)  # Перевірка
print("Check for the trapetzia method= ", round(v, 5))
