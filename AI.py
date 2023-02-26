import math as m

def calc(x, y):
    chose = input()
    if chose == '+':
        return x + y
    elif chose == '-':
        return x - y
    elif chose == '*':
        return x * y
    elif chose == '/':
        return x / y
    elif chose == 'e^(x+y)':
        return m.e**(x + y)
    elif chose == 'sin(x+y)':
        return m.sin(x + y)
    elif chose == 'cos(x+y)':
        return m.cos(x + y)
    elif chose == 'x^y':
        return x**y
    else:
        print("something wrong")


x = float(input())
y = float(input())
print(calc(x, y))
