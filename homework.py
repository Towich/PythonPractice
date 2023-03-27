import matplotlib.pyplot as plt
import numpy as np
from random import randint


def f(ind_i, ind_j, a, n, m):
    for i in range(ind_i, ind_i + n):
        for j in range(0, (m + 1) // 2):
            a[i][ind_j + j] = randint(0, 1)
            a[i][ind_j + m - j - 1] = a[i][ind_j + j]


N, M = 5, 5
a = np.zeros(N * M).reshape(N, M)
f(0, 0, a, N, M)
plt.figure(figsize=(10, 10))
plt.imshow(a, cmap="binary")
plt.show()
