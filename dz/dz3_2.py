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


# %%
o = LogisticMap(mu=2, state=0.1)
print(o.__next__())
print(o.__next__())
print(o.__next__())