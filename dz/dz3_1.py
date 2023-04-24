import graphviz

def draw(vertices, edges):# передаем узлы и грани
    dot = graphviz.Digraph() #граф
    for v in vertices: #добавляем узлы
        dot.node(str(v[0]), label=v[1]) #еще и название передаем
    for e in edges: # пути НЕ ПУТЮ
        dot.edge(str(e[0]), str(e[1]))
    return dot

vertices = [(1, 'v1'), (2, 'v2')]
edges = [(1, 2), (2, 3), (2, 2)]

graph = draw(vertices, edges)
print(graph)


