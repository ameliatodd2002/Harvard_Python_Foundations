import numpy as np

max_num = 9

matrix = np.zeros((max_num,max_num))

for i in range (1,max_num):
    for j in range(i):
        matrix[i][j] = i*100+(j-1)**2

print(matrix)