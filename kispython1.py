import math


def task1(z, y, x):
    a = math.sqrt(math.cos(1 + x + y * y) ** 7
                  + 34 * math.exp(51 - 77 * x - z ** 3) ** 4)
    b = x * x - 65 * (24 + y * y + 19 * z ** 3) ** 6
    return a + b

# print(task1(-0.73, -0.19, -0.87))
# print(task1(-0.18, 0.09, 0.69))
# print(task1(-0.96, -0.46, -0.47))
# print(task1(-0.56, -0.23, -0.02))
# print(task1(-0.03, -0.63, -0.72))


def task2(z):
    if z < 137:
        return 4 * (59 + z)**3
    elif z < 227:
        return 1 - 26 * (z**3 / 2 - 17 * z*z - 1)**3
    elif z < 295:
        return 88 * (97 * z - 1)**3
    elif z < 363:
        return 1 + (76 * z**3)**7/38
    else:
        return 70 * z**5 + 29 * math.cos(71 - 5 * z*z - 35 * z) + abs(z)**4


# print(task2(114))
# print(task2(338))
# print(task2(129))
# print(task2(315))
# print(task2(181))

def task3(n, m, b):
    summ = 0
    for j in range(1, b+1):
        for i in range(1, m+1):
            for k in range(1, n+1):
                summ += 87 * (i**3 / 8 + 1 + k)**4 - 28 * j**5 - 56 * j
    return summ


# print(task3(5, 3, 8))
# print(task3(2, 3, 8))
# print(task3(2, 6, 8))
# print(task3(7, 2, 3))
# print(task3(6, 4, 3))


def task4(n):
    if n == 0:
        return 0.74
    elif n >= 1:
        return (task4(n-1)**2 / 13 - task4(n-1))**2 - 1


# print(task4(3))
# print(task4(7))
# print(task4(5))

def task5(z, y, x):
    summ = 0
    n = len(z)

    for i in range(1, n+1):
        summ += 90 * math.log((z[n - i]**3 - y[math.ceil(i / 3) - 1] - x[math.ceil(i / 4) - 1]**2), 2)**6

    return summ


print(task5([-0.25, -0.75, 0.91],
            [-0.68, -0.24, 0.64],
            [0.03, 0.25, 0.62]))
print(task5([0.41, -0.19, 0.28],
            [-0.98, -0.64, 0.46],
            [0.46, 0.78, 0.47]))
