import numpy as np

matrix = np.random.randint(1, 11, size=(5, 5))

row_sums = np.sum(matrix, axis=1)

print("Matrix:")
print(matrix)

print ("Row-wise sums:")
print(row_sums)
