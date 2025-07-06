import numpy as np

array_1d = np.array([1, 2, 3, 4, 5])
array_2d = np.array([[1, 2, 3], [4, 5, 6]])


print("\nSlicing 1D array (1:4):", array_1d[1:4])
print("Slicing 2D array (row 1):", array_2d[1])
print("Slicing 2D array element [1][2]:", array_2d[1][2])
