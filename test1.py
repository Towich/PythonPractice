a = [[1, 3, 5], [1, 3, 15]]

def fun(a):
    return [sum(a[i]) for i in range(len(a))]

print(fun(a))