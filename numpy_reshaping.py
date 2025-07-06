import numpy as np

array_1d = np.array([1, 2, 3, 4, 5])

reshaped = np.reshape(array_1d, (5, 1))
print("\nReshaped 1D to 2D (5x1):\n", reshaped)