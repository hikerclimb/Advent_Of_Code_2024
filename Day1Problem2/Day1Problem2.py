import numpy as np
data = np.genfromtxt("input.txt", delimiter = None)
transposed = data.T
sort = np.sort(transposed)
#print(sort)
multiplicationsum = 0
counter = 0
for x in sort[0]:
    for y in sort[1]:
        if x == y:
            counter = counter + 1;
    multiplicationsum += x * counter
    counter = 0
print(multiplicationsum)
