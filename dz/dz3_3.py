import graphviz


class chaos:
    mu = 0.0
    state = 0.0

    def __init__(self, mu, state):
        self.mu = mu
        self.state = state
        self.stabilaize()

    def stabilaize(self):
        for i in range(1000):
            self.__next__()

    def __next__(self):
        self.state = self.mu * self.state


class LogisticMap(chaos):

    def __next__(self):
        self.state = self.mu * (1 - self.state) * self.state
        return self.state


def draw(vertices, edges):
    dot = graphviz.Digraph()
    for v in vertices:
        dot.node(str(v[0]), label=v[1])
    for e in edges:
        dot.edge(str(e[0]), str(e[1]))
    return dot


o = LogisticMap(mu=3.5, state=0.1)


def visualize(Map): # Визуализируем карту
    verts = set()
    edges = []
    i = 0
    j = 0
    while True:
        vert = Map.__next__()
        if vert in verts:
            break
        verts.add(vert)
        print(i, vert)
        edges.append((i, i + 1))
        i += 1

    edges.remove((i - 1, i))
    edges.append((i - 1, j))
    vertices = []
    i = 0
    for vert in verts:
        vertices.append((i, str(vert)))
        i += 1

    return draw(vertices, edges)

print(visualize(o))