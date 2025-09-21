from graphUtils import Graph

def unDirectedpath(edges, nodeA, nodeB):
    my_graph = Graph(edges)
    return hasPath(my_graph.get_graph(), nodeA, nodeB, set())

def hasPath(graph, src, dst, visited):
    if src == dst:
        return True

    if src in visited:
        return False

    visited.add(src)

    for neighbor in graph.get(src, []):
        if hasPath(graph, neighbor, dst, visited) == True:
            return True

    return False

testcase1 = [
    ['i', 'j'],
    ['k', 'i'],
    ['m', 'k'],
    ['k', 'l'],
    ['o', 'n']
]
# Create an instance of the Graph class
#my_graph = Graph(testcase1)

print("k->l tryint to see connection between valid nodes")
print("HappyPath: ", "--", unDirectedpath(testcase1, 'k', 'l'))

print("\n")
print("k->a(node doesnt exist in graph)")
print(f"UnHappyPath - trying with node not in the graph : --{unDirectedpath(testcase1, 'k', 'a')}")
