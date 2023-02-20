import math
import matplotlib.pyplot as matplotlib


def t1(n, m):
    sum1 = 0
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            sum1 += math.ceil(i) - 76 * j
    sum1 *= 22

    sum2 = 0
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            sum2 += (42 * j + 90 * j ** 4 - 8)

    sum2 /= 31

    return sum1 - sum2


print(t1(88, 80))
print(t1(21, 83))

def t2(n):
    if n == 0:
        return 6
    elif n == 1:
        return 4
    return 1 / 45 * t2(n - 2) ** 3 + math.cos(t2(n - 1))


print(t2(12))
print(t2(2))


def t3(y, z):
    n = len(y)
    sum = 0
    for i in range(1, n + 1):
        sum += (y[i - 1] - z[i - 1]) ** 2
    return math.sqrt(sum)


print(t3([1,  0.5, 1], [0.5, 2, 1]))


def t4(y, z):
    n = len(y)
    sum = 0
    for i in range(1, n + 1):
        sum += abs(y[i - 1] - z[i - 1])
    return sum


print(t4([1,  0.5, 1], [0.5, 2, 1]))


def t5(y, z):
    n = len(y)
    maxim = y[0]
    for i in range(1, n + 1):
        local_dist = abs(y[i - 1] - z[i - 1])
        if maxim < local_dist:
            maxim = local_dist
    return maxim


print(t5([1,  0.5, 1], [0.5, 2, 1]))

def t6(y, z):
    n = len(y)
    sum = 0
    for i in range(1, n + 1):
        sum += (y[i - 1] - z[i - 1]) ** 2
    return sum


print(t6([1,  0.5, 1], [0.5, 2, 1]))


def t7(y, z):
    h = 5
    n = len(y)
    sum = 0
    for i in range(1, n + 1):
        sum += abs(y[i - 1] - z[i - 1]) ** h
    return sum ** (1 / h)


print(t7([1,  0.5, 1], [0.5, 2, 1]))


def euclidean_distance(y, z):
    n = len(y)
    summ = 0
    for i in range(1, n + 1):
        summ += (y[i - 1] - z[i - 1]) ** 2
    return math.sqrt(summ)


def manhattan_distance(y, z):
    n = len(y)
    summ = 0
    for i in range(1, n + 1):
        summ += math.fabs(y[i - 1] - z[i - 1])
    return summ


def chebyshuov_distance(y, z):
    n = len(y)
    maximum = y[0]
    for i in range(1, n + 1):
        local_dist = abs(y[i - 1] - z[i - 1])
        if maximum < local_dist:
            maximum = local_dist
    return maximum


def square_euclidean_distance(y, z):
    sixth_ans = 0
    n = len(y)
    for i in range(0, n):
        sixth_ans += (y[i] - z[i]) ** 2
    return sixth_ans


def minkovskiy_distance(y, z):
    n = len(y)
    h = 5
    result = 0
    for i in range(0, n):
        result += math.fabs((y[i] - z[i]) ** h)
    return result ** (1 / h)


def visualize(distance_metrics, y, z, move=1):
    moved_z = [i + move for i in z]
    distance_differences = []
    for distance in distance_metrics:
        distance_before_move = distance(y, z)
        distance_after_move = distance(y, moved_z)
        distance_difference = distance_after_move - distance_before_move
        distance_differences.append(distance_difference)
    x = range(0, len(distance_differences))
    figure, axis = matplotlib.subplots()
    # построение гистограммы с подписями
    axis.bar(x, distance_differences)
    axis.set_xticks(x, labels=[f'd_{i + 1}' for i in x])


distance_metrics = [euclidean_distance, manhattan_distance, chebyshuov_distance, square_euclidean_distance, minkovskiy_distance]
visualize(distance_metrics, [1, 0.5, 1], [0.5, 2, 1], 1)
# matplotlib.show()

words = ["language!", "programming", "Python", "the", "love", "I"]


def t9(words):
    result = ""
    n = len(words)
    for i in range(n-1, -1, -1):
        result += words[i]
        if i != 0:
            result += " "
    return result


print(t9(words))


def t10(s, c):
    count = 0
    for i in s:
        if i == c:
            count += 1
    return count


def count_characters(s):
    dict = {}
    s = s.lower()
    for i in range(0, len(s)):
        key = s[i]
        if not (key in dict):
            value = t10(s, key)
            dict[key] = value
    return dict


print(count_characters('Hello world'))


def levenshtein(a, b, i, j):
    if (i == 0 or j == 0):
        return max(i, j)
    elif (a[i - 1] == b[j - 1]):
        return levenshtein(a, b, i - 1, j - 1)
    else:
        return 1 + min(levenshtein(a, b, i - 1, j), levenshtein(a, b, i, j - 1), levenshtein(a, b, i - 1, j - 1))


print(levenshtein('Hello, world!', 'Goodbye, world!', 1, 2))
