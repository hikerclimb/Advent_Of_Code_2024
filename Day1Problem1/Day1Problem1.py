import numpy as np
data = np.genfromtxt("input.txt", delimiter=None)
transposed = data.T
sort = np.sort(transposed)
print(sort)
result = sort[1] - sort[0]
print(result)
total = np.sum(np.absolute(result))
print(total)
