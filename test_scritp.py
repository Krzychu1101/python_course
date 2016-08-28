import numpy as np
import matplotlib.pyplot as plt

import os




array = [1, 3, 5, 6, 9, 11]

numpyArray = np.array(array)

numpyArray2 = np.sin(array) + np.cos(numpyArray)


plt.figure()
plt.plot(numpyArray, numpyArray2, ".",  markersize=20)
plt.show()