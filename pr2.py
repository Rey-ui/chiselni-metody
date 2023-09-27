import math
import numpy as np
from scipy.misc import derivative


def f(x):
    return 2 * x**4 + 4 * x**3 - x**2 - 3 * x - 1


eps = 0.0001


def fsegments():  # Відокремлюємо корені
    search_range = np.arange(-10, 10, 1)
    a = None
    previousx = None
    currentx = None
    segments = []

    for x in search_range:
        x = round(x, 4)
        currentx = f(x)
        if previousx is not None and previousx * currentx < 0:
            segments.append((a, x))
        a = x
        previousx = currentx
    return segments


def rec(a, b, eps):  # Метод половинного ділення
    while abs(a - b) > eps:
        if f(a) * f((a + b) / 2) < 0:
            b = (a + b) / 2
        else:
            a = (a + b) / 2
        x = (a + b) / 2
    return x


def hord(a, b, eps):  # Метод хорд
    if f(a) * derivative(f, a, n=2) > 0:
        x0 = a
        xi = b
    else:
        x0 = b
        xi = a
    xi_1 = xi - (xi - x0) * f(xi) / (f(xi) - f(x0))
    while abs(xi_1 - xi) > eps:
        xi = xi_1
        xi_1 = xi - (xi - x0) * f(xi) / (f(xi) - f(x0))
    return xi_1


segments = fsegments()

for segment in segments:
    a, b = segment
    print(f"Solution on segment [{a}, {b}]:")
    root_rec = rec(a, b, eps)
    print(f"Method of halves: x= {root_rec:.5f}")
    root_hord = hord(a, b, eps)
    print(f"Chord method: x= {root_hord:.5f}")
