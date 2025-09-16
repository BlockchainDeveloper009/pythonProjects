vertices = ['A','B','C', 'D', 'E']
vertexIdxs = {
'A': 0,
'B': 1,
'C': 2,
'D': 3,
'E': 4,

}

"""
A-------B
|     /   
|   C
| /   \
D------ E
"""
#above graph is represented in belwo form
adjacencyMatrix = [
    [0,1,0,1,0],
    [0,0,1,0,0],
    [0,1,0,1,1],
    [1,0,1,0,1],
    [0,0,1,1,0]
]

"""
# get tehe row in the matrix
# loop trhough the row
# if there is 1, push that cnode
# otherwise skip

"""

def findAdjacencies(node):
    adjacentNodes = []

    for i in range(len(vertices)):
        nodeVertex = vertexIdxs[node]
        if adjacencyMatrix[nodeVertex][i] == 1 :
            adjacentNodes.append(vertices[i])





    return adjacentNodes

def isConnected(node1, node2):
    nodeIdx1 = vertexIdxs[node1]
    nodeIdx2 = vertexIdxs[node2]

    return adjacencyMatrix[nodeIdx1][nodeIdx2]




class Graph_AdjacencyList:


