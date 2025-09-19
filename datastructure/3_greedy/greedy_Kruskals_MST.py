# A utility class for the Union-Find data structure.
# This structure is used to efficiently detect cycles.
class UnionFind:
    def __init__(self, vertices):
        # Initialize each vertex as its own parent and a rank of 0.
        # The parent array is used to find the root of a set.
        self.parent = list(range(vertices))
        # The rank array is used to keep the tree small during a union.
        self.rank = [0] * vertices

    # Find the root of the set a node belongs to.
    # It uses path compression for optimization.
    def find(self, i):
        if self.parent[i] == i:
            return i
        # Path Compression: Set the parent of i to the root of its set.
        self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    # Union two sets based on their ranks.
    # This prevents the tree from becoming too tall.
    def union(self, i, j):
        root_i = self.find(i)
        root_j = self.find(j)

        # If the roots are different, the vertices are not yet in the same set.
        if root_i != root_j:
            # Union by rank: Attach the smaller tree to the root of the larger tree.
            if self.rank[root_i] < self.rank[root_j]:
                self.parent[root_i] = root_j
            elif self.rank[root_i] > self.rank[root_j]:
                self.parent[root_j] = root_i
            else:
                # If ranks are the same, make one the new root and increment its rank.
                self.parent[root_j] = root_i
                self.rank[root_i] += 1
            return True  # Union was successful
        return False  # A cycle would have been formed


# The main Graph class and Kruskal's algorithm implementation.
class Graph:
    def __init__(self, vertices):
        self.V = vertices  # Number of vertices
        self.graph = []  # List to store edges (u, v, weight)

    # Function to add an edge to the graph.
    def add_edge(self, u, v, w):
        self.graph.append([u, v, w])

    # The main function that constructs the MST using Kruskal's algorithm.
    def kruskal_mst(self):
        result = []  # This list will store the edges of the MST.
        i = 0  # Index for the sorted graph edges.
        e = 0  # Index for the result array.

        # Step 1: Sort all the edges by weight in ascending order.
        self.graph = sorted(self.graph, key=lambda item: item[2])

        # Initialize the Union-Find data structure.
        uf = UnionFind(self.V)

        # Step 2: Iterate until we have V-1 edges in the MST.
        while e < self.V - 1:
            u, v, w = self.graph[i]
            i += 1

            # Find the roots of the two vertices.
            x = uf.find(u)
            y = uf.find(v)

            # Step 3: If the vertices are in different sets (no cycle), add the edge.
            if x != y:
                e += 1
                result.append([u, v, w])
                uf.union(x, y)  # Merge the two sets.

        # Print the edges of the constructed MST.
        print("Following are the edges in the constructed MST:")
        for u, v, weight in result:
            print(f"{u} -- {v}: {weight}")


# --- Example Usage ---
g = Graph(4)
g.add_edge(0, 1, 10)
g.add_edge(0, 2, 6)
g.add_edge(0, 3, 5)
g.add_edge(1, 3, 15)
g.add_edge(2, 3, 4)

g.kruskal_mst()