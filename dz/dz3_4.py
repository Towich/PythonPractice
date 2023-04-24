import numpy as np
import matplotlib.pyplot as plt


class chaos:
    mu = 0.0
    state = 0.0

    def __init__(self, mu, state): #  передаем параметры и состояние, стабилизируем
        self.mu = mu
        self.state = state
        self.stabilaize()

    def stabilaize(self):
        for i in range(1000):
            self.__next__()

    def __next__(self):
        self.state = self.mu * self.state


class LogisticMap(chaos): #переопределение метода перехода по формуле

    def __next__(self):
        self.state = self.mu * (1 - self.state) * self.state
        return self.state


x_s = []
y_s = []
a = set()
for i in np.arange(1, 4.0, 0.1):
    Map = LogisticMap(mu=round(i, 2), state=0.1) #создаем обжект класса  с параметром счетчика
    a.clear() #на всякий случай очищаем
    q = - 1
    while True: #цикл ищет все состояния, как только нашли повтор - финиш все
        q = round(Map.__next__(), 2)
        if q in a:
            break
        a.add(q)
    for el in a: #для каждого элемента состояний
        x_s.append(i) #где мы находимся
        y_s.append(el) #добавляем каждое состояние

fig, ax = plt.subplots()

ax.scatter(x_s, y_s, color = "pink")

plt.show()