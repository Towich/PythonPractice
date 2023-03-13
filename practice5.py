def smalldet(A):
    return A[0][0] * A[1][1] - A[0][1] * A[1][0]


print(smalldet([[4, 3], [1, 1]]))


def submatrix(A, i, j):
    local_i = 0
    local_j = 0

    n = len(A)
    B = [0] * (n-1)
    for m in range(n-1):
        B[m] = [0] * (n-1)

    local_B = [0] * (n-1) * (n-1)
    local_count = 0

    for k in range(0, n):
        for l in range(0, n):
            if k == i or l == j:
                continue
            local_B[local_count] = A[k][l]
            local_count += 1

    counter1 = 0
    for il in range(0, n-1):
        for jl in range(0, n-1):
            B[il][jl] = local_B[counter1]
            counter1 += 1

    return B


print(submatrix([[0, 2, 1], [1, 4, 3], [2, 1, 1]], 1, 1))


def det(A, i=0):
    if len(A) == 2:
        return smalldet(A)

    sum = 0
    n = len(A)

    for j in range(0, n):
        sum += (-1)**(i + j) * A[i][j] * det(submatrix(A, i, j))

    return sum


A = [[0, 2, 1, 4], [1, 0, 3, 2], [0, 1, 4, 0], [1, 2, 1, 1]]
print(det(A, 0))


def minor(A, i, j):
    return det(submatrix(A, i, j))


print(minor(A, 0, 1))


def alg(A, i, j):
    return (-1)**(i+j) * minor(A, i, j)


print(alg(A, 1, 1))


def algmatrix(A):
    n = len(A)

    B = [0] * n
    for l in range(n):
        B[l] = [0] * n

    for i in range(n):
        for j in range(n):
            B[i][j] = alg(A, i, j)

    return B


print(algmatrix(A))


def transpose(A):
    n = len(A)

    B = [0] * n
    for l in range(n):
        B[l] = [0] * n

    for i in range(n):
        for j in range(n):
            B[i][j] = A[j][i]

    return B


print(transpose(A))

def inv(A):
    n = len(A)

    B = transpose(A)
    B = algmatrix(B)

    for i in range(n):
        for j in range(n):
            B[i][j] = B[i][j] / det(A)
    return B


print(inv(A))


def mult(A, B):
    length = len(A)
    C = [[0 for i in range(length)] for i in range(length)]
    for i in range(length):
        for j in range(length):
            for k in range(length):
                C[i][j] += A[i][k] * B[k][j]

    return C


A1 = [[4, 2], [9, 0]]
B1 = [[3, 1], [-3, 4]]

#print(mult(A1, B1))


def moore_penrose(A):
    return mult(inv(mult(transpose(A), A)), transpose(A))


print(moore_penrose(A))