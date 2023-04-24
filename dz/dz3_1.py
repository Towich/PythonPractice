import graphviz


def draw(vertices, edges):
    dot = graphviz.Digraph()
    for v in vertices:
        dot.node(str(v[0]), label=v[1])
    for e in edges:
        dot.edge(str(e[0]), str(e[1]))
    return dot


vertices = [(1, 'v1'), (2, 'v2')]
edges = [(1, 2), (2, 3), (2, 2)]

graph = draw(vertices, edges)
print(graph)


