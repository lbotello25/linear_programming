import numpy as np


I = np.identity(n=M)  #Initialize Identity Matrix
aug_matrix = np.concatenate((matrix, I), axis = 1)
print('Augmented Matrix:')
print(np.round(aug_matrix, decimals=2))
print("-------*--------")

for i in range(M-1):
    pivot = aug_matrix[i][i]
    #Swap Rows so that diagonal has non-zero elements
    if pivot == 0:
        for k in range(i+1,M):
            if aug_matrix[k][i] != 0:
                temp = aug_matrix[i].copy()
                aug_matrix[i] = aug_matrix[k].copy()
                aug_matrix[k] = temp.copy()
                break


print('Re-Arranged Matrix:')
print(np.round(aug_matrix,decimals=2))


k=0
for j in range(0,M):   #Iterate over COLUMNS
    pivot = aug_matrix[k][k]
    for i in range(0,M):    #Iterate over ROWS
        if i == k:
            pass
        else:
            target = aug_matrix[i][j]
            multiplier = target/pivot
            aug_matrix[i] = aug_matrix[i] - multiplier*aug_matrix[j]
    k += 1



for i in range(M):
    divider = aug_matrix[i][i]
    aug_matrix[i] = aug_matrix[i]/divider