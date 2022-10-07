import numpy as np

def matTransNp(mat):
    mat = np.array(mat)
    mat = mat.transpose() #транспонирование
    return mat

def matMultNp(mat1,mat2):
    mat1 = np.array(mat1)
    mat2 = np.array(mat2)
    multiMat = mat1.dot(mat2) #умноженние первой на вторую
    return multiMat

def matRangNp(mat):
    mat = np.array(mat)
    matRang = np.linalg.matrix_rank(mat)
    return matRang

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
        print(*matTransNp(mat), sep ='\n')
    else:
        print(matRangNp(mat), sep ='\n')
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
    print(*matMultNp(mat1,mat2), sep = '\n')
