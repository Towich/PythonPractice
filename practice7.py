import numpy as np
import matplotlib.pyplot as plt

def funcX(t):
    return 16 * (np.sin(t))**3

def funcY(t):
    return 13 * np.cos(t) - 5 * np.cos(2*t) - 2 * np.cos(3*t) - np.cos(4*t)

def task1():
    t = np.arange(0, 2*np.pi, np.pi/24)
    plt.figure(figsize=(6, 6))

    plt.plot(funcX(t), funcY(t), 'red')
    plt.show()

    plt.figure(figsize=(6, 6))
    plt.fill(funcX(t), funcY(t), 'red')
    plt.show()


task1()


def task2():
    