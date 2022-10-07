import time
import numbers as np
mat = []
flag = input('Вы собираетесь умножать матрицы? (y|n): ')
if flag == 'n':
    flag = input('Вы считать ранг матрицы? (y|n): ')
    if flag == 'y': print('Введите матрицу 3х3, если вы хотите найти ранг матрицы')
    print('После ввода матрицы нажмите Enter')
    mat = []

    #Цикл заполнения матрицы
    while True:
        arr = list(map(int, input().split()))
        if arr == []:
            break
        mat.append(arr)
    if flag == 'n':
        mat = np.array(mat)
        mat = mat.transpose()
        print(*mat, sep ='\n')
    else:
        mat = np.array(mat)
        matRang = np.linalg.matrix_rank(mat)
        print(matRang, sep ='\n')
        
else:
    mat1 = []
    mat2 = []

    #Заполнение двух матриц
    while True:
        arr = list(map(int, input().split()))
        if arr == []:
            break
        mat1.append(arr)
    while True:
        arr = list(map(int, input().split()))
        if arr == []:
            break
        mat2.append(arr)
    mat1 = np.array(mat1)
    mat2 = np.array(mat2)
    multi = np.dot(mat1, mat2)
    print(*multi, sep = '\n')
