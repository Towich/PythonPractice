import math


def t1(n, m):
    sum1 = 0
    for i in range(1, n+1):
        for j in range(1, m+1):
            sum1 += math.ceil(i) - 76*j
    sum1 *= 22

    sum2 = 0
    for i in range(1, n+1):
        for j in range(1, m+1):
            sum2 += (42*j + 90*j**4 - 8)

    sum2 /= 31

    return sum1 - sum2


# print(t1(88, 80))
# print(t1(21, 83))

def t2(n):
    if n == 0:
        return 6
    elif n == 1:
        return 4
    return 1/45 * t2(n-2)**3 + math.cos(t2(n-1))


# print(t2(12))
# print(t2(2))


def t3(y, z):
    n = len(y)
    sum = 0
    for i in range(1, n+1):
        sum += (y[i-1] - z[i-1])**2
    return math.sqrt(sum)


# print(t3([1,  0.5, 1], [0.5, 2, 1]))


def t4(y, z):
    n = len(y)
    sum = 0
    for i in range(1, n + 1):
        sum += abs(y[i-1] - z[i-1])
    return sum


# print(t4([1,  0.5, 1], [0.5, 2, 1]))


def t5(y, z):
    n = len(y)
    maxim = y[0]
    for i in range(1, n + 1):
        local_dist = abs(y[i-1] - z[i-1])
        if maxim < local_dist:
            maxim = local_dist
    return maxim


print(t5([1,  0.5, 1], [0.5, 2, 1]))
