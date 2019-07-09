import numpy as np
import matplotlib.pyplot as plt

data = []
with open('build/out.txt', 'r') as ifile:
    for line in ifile:
        data.append(float(line.split()[-1]))

plt.hist(data, bins=100)
plt.show()
