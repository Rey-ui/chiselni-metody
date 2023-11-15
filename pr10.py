import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import least_squares


# Задана функція
def func(x):
    return np.sin(x + 1) + x


# Задані точки xi
x = np.array([i * 0.1 for i in range(10)])

# Знаходимо значення yi = f(xi)
y = np.array([func(xi) for xi in x])

# Виводимо значення xi та yi
print("xi =", x)
print("yi =", y)


# Функція, яку будемо наближати за МНК (параболою)
def fun_parabola(a, x, y):
    return a[0] + a[1] * x + a[2] * x**2 - y


# Початкове наближення для параметрів a (парабола)
a0_parabola = np.array([1, 1, 1])

# Застосовуємо МНК для параболі
res_lsq_parabola = least_squares(fun_parabola, x0=a0_parabola, args=(x, y))

# Виводимо отримані параметри для параболи
print("Парабола: a0 = %.2f, a1 = %.2f, a2 = %.2f" % tuple(res_lsq_parabola.x))

# Побудова графіку для параболи
f_parabola = lambda x: sum([u * v for u, v in zip(res_lsq_parabola.x, [1, x, x**2])])
x_p = np.linspace(min(x), max(x), 100)
y_parabola = f_parabola(x_p)

plt.plot(x, y, "o", label="Дані")
plt.plot(x_p, y_parabola, "b", label="МНК (Парабола)")
plt.title("МНК наближення функції (Парабола)")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid(True)
plt.show()


# Функція, яку будемо наближати за МНК (прямою)
def fun_line(a, x, y):
    return a[0] + a[1] * x - y


# Початкове наближення для параметрів a (пряма)
a0_line = np.array([1, 1])

# Застосовуємо МНК для прямої
res_lsq_line = least_squares(fun_line, x0=a0_line, args=(x, y))

# Виводимо отримані параметри для прямої
print("Пряма: a0 = %.2f, a1 = %.2f" % tuple(res_lsq_line.x))

# Побудова графіку для прямої
f_line = lambda x: res_lsq_line.x[0] + res_lsq_line.x[1] * x
y_line = f_line(x_p)

plt.plot(x, y, "o", label="Дані")
plt.plot(x_p, y_line, "r", label="МНК (Пряма)")
plt.title("МНК наближення функції (Пряма)")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid(True)
plt.show()
