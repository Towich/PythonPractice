import cmath
a = 4

def prog31(a):
    b = a + a
    a = b + b + b
    a += a
    return a


def prog32(a):
    b = a + a #8
    a = b + b #16
    a = a + a #32
    a = a + a #64
    return a

def prog33(a):
    b = a
    a = a + a  # 8
    a = a + a  # 16
    a = a + a  # 32
    b = b - a
    a = a - b
    return a

def prog34(b, n, a):
    s1 = 0
    s2 = 0
    s3 = 1
    for j in range(n):
        for c in range(b):
            s1 += ((34*j + 41)**4 - 93*(c + 79 + c**3)**5)


    for c in range(b):
        for k in range(a):
            s2 += 22 * (c - 8)** 5 - k ** 4
        s3 *= s2
    return s3

#print(prog34(2, 2, 6))

def prog35(x):
    if x < 13:
        return x**5
    elif x < 87:
        return x**7 - 1 - (int(x)**3 / 54)
    else:
        return int(x)**3

#print(prog35(12))

def prog36(n):
    if n == 0:
        return 3
    return cmath.sin((prog36(n-1))) - 1/16*(prog36(n-1))**3

#print(prog36(8))

def prog37(a, b):
    final = 0
    while a != 0:
        if a % 2 == 1:
            final += b
        a = a // 2
        b = b * 2
    return final

def fast_mul(a, b):
    result = 0
    step = 0

    a = bin(a)[2:]
    b = bin(b)[2:]

    for i in range(len(b)):
        if b[len(b) - i - 1] != '0':
            int10_a = int(a, 2) << step
            result += int10_a
        step += 1
    return result


# a = 10
# b = 15
# assert fast_mul(a, b) == a * b
# print(fast_mul(a, b))

def fast_pow(a, x):
    a = bin(a)[2:]
    b = a

    if x == 0:
        return 1

    elif x == 1:
        return int(a,2)

    for k in range(x-1):
        result = 0
        step = 0
        for i in range(len(b)):
            if b[len(b) - i - 1] != '0':
                int10_a = int(a, 2) << step
                result += int10_a
            step += 1
        a = bin(result)[2:]
    return result

# a = 2
# x = 9
# #assert fast_pow(a, x) == a**x
# print(fast_pow(a, x))

def fast_mul_gen(a, y):
    print("a =", a, "y =", y)
    result = fast_mul(a, y)  # 28

    local_a = a
    while a < result:
        a = a + a # 24
        print("a += a")

    diff = a - result  # 3

    while diff != 0:
        b = 1
        while b + b <= diff:
            b = b + b
            print("b += b")

        a -= b
        print("a -= b")

        diff = a - result  # 2

    return a

a = 3
y = 7

result_fast_mul_gen = fast_mul_gen(a, y)
assert result_fast_mul_gen == a * y
print("result =", result_fast_mul_gen)
