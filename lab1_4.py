import numpy as np
import timeit

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


def myFunction(mat):
    matminor = []    
    for i in range(len(mat)):
        arr = []
        for j in range(len(mat[0])):
            minor = matMinor(mat,j,i)
            arr.append(minor)
        matminor.append(arr)
        
    matminortrans = matTrans(matminor)

    opr = mat[0][0]*mat[1][1]*mat[2][2] + mat[1][0]*mat[2][1]*mat[0][2] + \
            mat[0][1]*mat[1][2]*mat[2][0] - mat[0][2]*mat[1][1]*mat[2][0] - \
            mat[0][1]*mat[1][0]*mat[2][2] - mat[0][0]*mat[1][2]*mat[2][1]
    if opr == 0:
        return 'Обратной нет'
    
    obrat = []
    for i in range(len(matminortrans)):
        arr = []
        for j in range(len(matminortrans[-1])):
            arr.append(1/opr*matminortrans[i][j])
        obrat.append(arr)
    return obrat

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
def antimatNumpy(mat):
    mat = np.array(mat_start)
    antimat = np.linalg.matrix_power(mat,-1)
    return antimat
mat_start = [[1,0,0],[0,1,-2],[0,0,1]]
'''while True:
    arr = list(map(int, input().split()))
    if arr == []:
        break
    mat.append(arr)'''
start_time = timeit.default_timer();
print(*myFunction(mat_start), sep = '\n')
range_time_1 = timeit.default_timer() - start_time
print(range_time_1)
print('--------------------------')
start_time = timeit.default_timer();
print(*antimatNumpy(mat_start), sep = '\n')
range_time_1 = timeit.default_timer() - start_time
print(range_time_1)
