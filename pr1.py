import math

x1 = 66
x2 = 7 / 3
x11 = 8.12
x22 = 2.33


def f(x1, x11, x2, x22):
    rel_x1 = abs(math.sqrt(x1) - x11) / abs(math.sqrt(x1))
    rel_x2 = abs(x2 - x22) / abs(x2)

    if rel_x1 < rel_x2:
        print("Перша рівність точніше з відносною похибкою:", rel_x1)
    elif rel_x2 < rel_x1:
        print("Друга рівність точніше з відносною похибкою:", rel_x2)
    else:
        print("Обидві рівності мають однакову точність з відносною похибкою:", rel_x1)


f(x1, x11, x2, x22)
