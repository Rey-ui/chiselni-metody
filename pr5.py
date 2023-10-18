import numpy as np
import matplotlib.pyplot as plt


def plot_equations():
    x_min, x_max = -3, 3
    y_min, y_max = -3, 3
    step = 0.01

    x, y = np.meshgrid(np.arange(x_min, x_max, step), np.arange(y_min, y_max, step))

    eq1 = np.cos(y - 1) + x - 0.8
    eq2 = y - np.cos(x) - 2

    fig, ax = plt.subplots(figsize=(10, 10))

    ax.contour(x, y, eq1, levels=[0], colors="red")
    ax.contour(x, y, eq2, levels=[0], colors="blue")

    ax.set_xlim([x_min, x_max])
    ax.set_ylim([y_min, y_max])
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_title("Графік системи рівнянь")
    plt.grid(True)

    plt.show()


# Виклик функції для побудови графіка
plot_equations()
import numpy as np
from scipy import optimize


def simple_iteration(x0, y0, e):
    def f1(y):
        return 0.8 - np.cos(y)

    def f2(x):
        return 2 + np.cos(x)

    def iteration(x, y):
        xn1 = f2(x)
        yn1 = f1(y)
        return xn1, yn1

    xn, yn = x0, y0
    n = 1

    while True:
        xn1, yn1 = iteration(xn, yn)
        if abs(xn1 - xn) < e and abs(yn1 - yn) < e:
            break
        xn, yn = xn1, yn1
        n += 1

    print("Simple iteration:")
    print("x=", xn, "\ny=", yn, "\nThe amount of iteration = ", n)


# Виклик функції для методу простої ітерації
simple_iteration(0.15, -2.1, 0.001)
from scipy import optimize


def check_solution():
    def f3(x):
        return np.array([np.cos(x[1] - 1) + x[0] - 0.8, x[1] - np.cos(x[0]) - 2])

    result = optimize.root(f3, [0.0, 0.0], method="hybr")
    print("Check", result.x)


# Виклик функції для перевірки розв'язку
check_solution()
