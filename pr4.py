import numpy as np

# Завдання 1: 1)Знайти матрицю C = AB - BA
A = np.array([[1, 2], [4, -1]])
B = np.array([[2, -3], [-4, 1]])
C = np.dot(A, B) - np.dot(B, A)
print("Завдання 1: Знайти матрицю C = AB - BA:")
print(C)

# Завдання 2: 2)Піднести матриці до степеня
D = np.array([[-1, 0, 2], [0, 1, 0], [1, 2, -1]])
D_squared = np.linalg.matrix_power(D, 2)
print("Завдання 2: Піднести матрицю D до квадрату:")
print(D_squared)

# Завдання 3: 1)Знайти добуток матриць
E = np.array([[3, 5], [6, -1]])
F = np.array([[2, 1], [-3, 2]])
G = np.dot(E, F)
print("Завдання 3: Знайти добуток матриць E та F:")
print(G)

# Завдання 4: 3)Обчислити визначник
det_4 = np.linalg.det([[2, 4, 5], [1, 1, 2], [2, 4, 3]])
print("Завдання 4: Обчислити визначник матриці:")
print(det_4)

# Завдання 5: 2)Обчислити визначник
det_5 = np.linalg.det([[2, 3, 4, 1], [1, 2, 3, 4], [3, 4, 1, 2], [4, 1, 2, 3]])
print("Завдання 5: Обчислити визначник матриці:")
print(det_5)

# Завдання 6: 1)Знайти обернену матрицю
H = np.array([[1, 2, -3], [0, 1, 2], [0, 0, 1]])
H_inv = np.linalg.inv(H)
print("Завдання 6: Знайти обернену матрицю до H:")
print(H_inv)

# Завдання 7: 1)Визначити ранг матриці
I = np.array([[1, 2, 3, 4], [3, -1, 2, 5], [1, 2, 3, 4], [1, 3, 4, 5]])
rank_I = np.linalg.matrix_rank(I)
print("Завдання 7: Визначити ранг матриці I:")
print(rank_I)

# Завдання 8: 29)Розвязати систему лінійних рівнянь
J = np.array([[2, -1, 1], [3, 4, -2], [1, -3, 1]])
K = np.array([5, -3, 4])


# Метод Крамера
def kram(a, b):
    det_a = np.linalg.det(a)
    if det_a != 0:
        a1, a2, a3 = np.array(a), np.array(a), np.array(a)
        a1[:, 0], a2[:, 1], a3[:, 2] = b, b, b
        x = np.linalg.det(a1) / det_a
        y = np.linalg.det(a2) / det_a
        z = np.linalg.det(a3) / det_a
        print("Метод Крамера:")
        print("x =", x.round(3), "y =", y.round(3), "z =", z.round(3))
    else:
        print("Визначник дорівнює нулю")
    return x, y, z


# Матричний метод
J_inv = np.linalg.inv(J)
X = np.dot(J_inv, K)
print("Матричний метод:")
print("X=", X)
print("Checking with solve():", np.linalg.solve(J, K).round(3))

# Всі розв'язки
kram(J, K)


# Завдання 9: 1)Створити прямокутну матрицю та знайти елемент з максимальною сумою модулів у стовпці
def create_matrix(N, M):
    return np.random.randint(1, 10, size=(N, M))


def find_max_column_element(matrix):
    column_sums = np.sum(np.abs(matrix), axis=0)
    max_column_index = np.argmax(column_sums)
    max_element = np.max(np.abs(matrix[:, max_column_index]))
    return max_element


N, M = 3, 4
A_9 = create_matrix(N, M)
max_element = find_max_column_element(A_9)
print("Знайти найменший стовпчастий елемент матриці A_9:")
print("Matrix A_9:")
print(A_9)
print("Max absolute sum column element:", max_element)
