import matplotlib.pyplot as plt
import numpy as np
from random import randint


def f(ind_i, ind_j, a, n, m):
    for i in range(ind_i, ind_i + n):
        for j in range(0, (m + 1) // 2):
            a[i][ind_j + j] = randint(0, 1)
            a[i][ind_j + m - j - 1] = a[i][ind_j + j]
n = 100
m = 200
N = 5
M = 5
a = np.ones(n * m).reshape(n, m)

for i in range(0, n, N * 2):
    for j in range(0, m, M * 2):
        f(i, j, a, N, M)

plt.figure(figsize=(20, 20))
plt.imshow(a, cmap="binary")
plt.show()
