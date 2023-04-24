import graphviz


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

def draw(vertices, edges):# передаем узлы и грани
    dot = graphviz.Digraph() #граф
    for v in vertices: #добавляем узлы
        dot.node(str(v[0]), label=v[1]) #еще и название передаем
    for e in edges: # пути НЕ ПУТЮ
        dot.edge(str(e[0]), str(e[1]))
    return dot

o = LogisticMap(mu=3.5, state=0.1) # создаем обжект


def visualize(Map): #визуализируем карту
    verts = set() #узлы без повторов
    edges = [] #грани (список)
    i = 0
    j = 0
    while True: #пока есть новые узлы - аппенд
        vert = Map.__next__()
        if vert in verts:
            break
        verts.add(vert)
        print(i, vert)
        edges.append((i, i + 1)) #создаем грань
        i += 1

    edges.remove((i - 1, i)) #убираем лишние грани
    edges.append((i - 1, j)) #добавляем "вернуться в начальное состояние"
    vertices = [] #пустой список граней
    i = 0
    for vert in verts: #формируем список граней с названиями
        vertices.append((i, str(vert)))
        i += 1

    return draw(vertices, edges)

print(visualize(o))