import numpy as np
n, m = map(int, input('Размерность первого массива: ').split())
a, b = map(int, input('Размерность второго массива: ').split())
if n > 10 or m > 10:
    print('Массив n, m больше 10x10')
    exit()
if a > 10 or b > 10:
    print('Массив a, b больше 10x10')
    exit()
matrix1 = np.random.randint(-10, 10, (n, m))
matrix2 = np.random.randint(-10, 10, (a, b))
print('Первый массив: ')
print(matrix1)
print('Второй массив: ')
print(matrix2)
poloj = []
for i in range(m):
    poloj_cons = True
    for j in range(n):
        if matrix1[j, i] < 0:
            poloj_cons = False
    if poloj_cons:
        poloj.append(i)
poloj2 = []
for i in range(b):
    poloj_cons = True
    for j in range(a):
        if matrix2[j, i] < 0:
            poloj_cons = False
    if poloj_cons:
        poloj2.append(i)
if poloj:
    print("Номера столбцов только с положительными элементами в первом массиве:", poloj)
else:
    print("Нет столбцов только с положительными элементами в первом массиве.")
if poloj2:
    print("Номера столбцов только с положительными значениями во втором массиве:", poloj2)
else:
    print("Нет столбцов только с положительными значениями во втором массиве.")
