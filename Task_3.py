# Задание 3
# Матричные операции
# Вариант 17
# Выражение: G=C(A-BE^2)D+B
# x1 = 44.85
# x2 = 47.58
# n = 4
# m = 5

import pandas as pd
import numpy as np


# Определение матрицы A со случайными вещественными значениями от 0 до 1
def matrix_A():
    n = 5
    m = 5
    A = np.random.random((n, m))
    return A


# Определение матрицы B со случайными вещественными значениями от 0 до 1
def matrix_B():
    n = 5
    m = 5
    B = np.random.random((n, m))
    return B


# Определение матрицы C со случайными вещественными значениями от 0 до 1
def matrix_C():
    n = 5
    m = 5
    C = np.random.random((n, m))
    return C


# Определение матрицы D со случайными вещественными значениями от 0 до 1
def matrix_D():
    n = 5
    m = 5
    D = np.random.random((n, m))
    return D


# Определение матрицы E со случайными вещественными значениями от 0 до 1
def matrix_E():
    n = 5
    m = 5
    E = np.random.random((n, m))
    return E


# Вычисление матричного выражения
def matrix_expression(A, B, C, D, E):
    return C.dot(A - B.dot(E.dot(E))) + D + B


# Основная функция программы
if __name__ == '__main__':
    x1 = 44.85
    x2 = 47.58
    n = 4
    m = 5
    A = matrix_A()
    B = matrix_B()
    C = matrix_C()
    D = matrix_D()
    E = matrix_E()
    G = matrix_expression(A, B, C, D, E)
    G_x1 = G + x1
    G_x2 = G - x2
    det_G = np.linalg.det(G)
    rev_G = np.linalg.inv(G)
    test_G = np.round(np.dot(G, rev_G))
    rank_G = np.linalg.matrix_rank(G)
    eigvals_G = np.linalg.eigvals(G)
    eig_G = np.linalg.eig(G)[1]
    diag_G = np.diag(G)

    A_2 = G[n-1]
    B_2 = G[:, m-1]
    norm_A_2 = np.linalg.norm(A_2)
    norm_B_2 = np.linalg.norm(B_2)
    ort_A_2 = A_2 / norm_A_2
    ort_B_2 = B_2 / norm_B_2
    y = np.arccos(np.dot(A_2, B_2) / (norm_A_2 * norm_B_2))

    print("A = \n", pd.DataFrame(A))
    print("B = \n", pd.DataFrame(B))
    print("C = \n", pd.DataFrame(C))
    print("D = \n", pd.DataFrame(D))
    print("E = \n", pd.DataFrame(E))
    print("G = \n", pd.DataFrame(G))
    print("G + x1 = \n", pd.DataFrame(G_x1))
    print("G - x2 = \n", pd.DataFrame(G_x2))
    print("Определитель матрицы G = ", det_G)
    print("Обратная матрица G = \n", pd.DataFrame(rev_G))
    print("Проверка обратной матрицы = \n", pd.DataFrame(test_G))
    print("Ранг матрицы G = ", rank_G)
    print("Собственные значения матрицы G = \n", pd.DataFrame(eigvals_G))
    print("Собственные векторы матрицы G = \n", pd.DataFrame(eig_G))
    print("Матрица собственных векторов * диагональная матрица G = \n", pd.DataFrame(np.dot(eig_G, diag_G)))
    print("Матрица G * матрица собсвтенных векторов = \n", pd.DataFrame(np.dot(G, eig_G)))
    print("A_2 = \n", pd.DataFrame(A_2))
    print("B_2 = \n", pd.DataFrame(B_2))
    print("Норма матрицы A_2 = ", norm_A_2)
    print("Норма матрицы B_2 = ", norm_B_2)
    print("Ортогональная матрица A_2 = \n", pd.DataFrame(ort_A_2))
    print("Ортогональная матрица B_2 = \n", pd.DataFrame(ort_B_2))
    print("Проверка ортогональности матриц A_2 и B_2:= ", np.dot(ort_A_2, ort_B_2))
    print("Сумма векторов A_2 и B_2:= ", (np.sum(A_2) + np.sum(B_2)))
    print("Кол-во положительных элементов в матрице A_2:= ", len(A_2[A_2 >= 0]))
    print("Кол-во положительных элементов в матрице B_2:= ", len(B_2[B_2 >= 0]))
    print("Кол-во отрицательных элементов в матрице A_2:= ", len(A_2[A_2 < 0]))
    print("Кол-во отрицательных элементов в матрице B_2:= ", len(B_2[B_2 < 0]))
    print("Скалярное произведение векторов A_2 и B_2:= ", np.dot(A_2, B_2))
    print("cos(y):= ", np.cos(y))
    print("sin(y):= ", np.sin(y))
    print("Перекрестное произведение векторов:= ", norm_A_2 * norm_A_2 * np.sin(y))
    print("Умножение векторных координат A_2 и B_2:=\n", pd.DataFrame(np.multiply(A_2, B_2)))




