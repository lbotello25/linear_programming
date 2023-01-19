from timeit import timeit
import scipy.sparse as sparse
import numpy as np


#Matrix Constructor Class
class matrix_gen:
    def __init__(self, rows, columns, density, lower_bound, upper_bound):
        self.rows = rows
        self.columns = columns
        self.density = density
        self.upper_bound = upper_bound
        self.lower_bound = lower_bound

    def norm_matrix(self):
        np.random.seed(1)
        return sparse.random(self.rows, self.columns, density=self.density).todense()

    def scaled_matrix(self):
        test = self.norm_matrix()
        return np.where(test>0,
                        (test*(self.upper_bound - self.lower_bound))+self.lower_bound,
                        test)


#Generate Random Matrix (10x10, density = 0.8)
B = matrix_gen(10,10,.8,-10,30).scaled_matrix()
#Check for all-zero rows and columns & for singularity.
counter = 1
while (~np.any(B>0, axis = 0)).any() == True or (~np.any(B>0, axis = 1)).any() == True or np.linalg.det(B) == 0:
    counter += 1
    print("Matrix is singular or an all-Zero row or column was detected, trial #:", counter)
    B = matrix_gen(10,10,.8,-10,30).scaled_matrix()


print('Scaled Matrix:')
print('determinant=', np.linalg.det(B))
print(np.round(B,decimals=2))


b = matrix_gen(10,1,.8,0,50).scaled_matrix()
print(np.round(b,decimals=2))


inv_B = np.linalg.inv(B)
complexity = %timeit np.linalg.inv(B)
print(complexity)


soln  = np.dot(inv_B,b)
print(np.round(soln,decimals=2))
