import numpy as np
x = np.ones((5,5))
print("Normal Array: \n", x)
print('\n')

x[1:-1, 1:-1] = 0


print(x)