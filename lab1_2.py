def matTrans(mat3):
    collums = len(mat3[0])
    rows = len(mat3)
    arr = []
    mat4 = []
    #Создаем новую матрицу
    for i in range(collums):
        for j in range(rows):
            arr.append(mat3[j][i])
        mat4.append(arr)
        arr = []
    return mat4

def matMulti(mat1,mat2):
    #Проверка возможности умножения
    if len(mat1[0]) != len(mat2):
        return 'Такие матрицы нельзя умножать'
    mat3 = []
    collums = len(mat2[0])
    rows = len(mat1)
    n = len(mat2)
    for i in range(rows):
        arr = []
        for j in range(collums):
            c = 0
            for k in range(n):
                #С11 С12 С13
                #C21 C22 C23 и тд,
                c += mat1[i][k]*mat2[k][j]
            #заполняем строку
            arr.append(c)
        mat3.append(arr)
        arr = []
    return mat3

def matRang(mat):
    #т.к. мы работает с матрицами 3х3, их ранг 0..3
    #Проверка на ранг = 0
    if all(mat[i][j] == 0 for i in range(len(mat)) for j in range(len(mat[i]))):
        return 0
    #Проверка на ранг = 3
    elif (mat[0][0]*mat[1][1]*mat[2][2] + mat[1][0]*mat[2][1]*mat[0][2] + \
        mat[0][1]*mat[1][2]*mat[2][0] - mat[0][2]*mat[1][1]*mat[2][0] - \
        mat[0][1]*mat[1][0]*mat[2][2] - mat[0][0]*mat[1][2]*mat[2][1]) != 0:
        return 3
    #Проверка на ранг = 2
    elif any(matMinor(mat,x,y) for x in range(len(mat[0])) for y in range(len(mat)))\
        != 0: return 2
    #Оставшийся вариант
    else:
        return 1
        

#Функция поиска миноров в матрице 3х3
def matMinor(mat,collum,row):
    mat_new = []
    for i in range(len(mat)):
        arr = []
        for j in range(len(mat[-1])):
            if j != collum and i != row:
                arr.append(mat[i][j])
        if arr:
            mat_new.append(arr) 
    return ((-1)**(collum+row+2)*(mat_new[0][0]*mat_new[1][1] - mat_new[0][1]*mat_new[1][0]))



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
        print(*matTrans(mat), sep = '\n')
    else:
        rang = matRang(mat)
        print(rang)
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
    print(*matMulti(mat1,mat2), sep = '\n')
