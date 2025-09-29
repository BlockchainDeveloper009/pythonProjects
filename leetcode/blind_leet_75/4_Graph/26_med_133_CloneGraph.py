n
class Node:
    def __init__(self, val: int = 0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

def cloneGraph(node: 'Node') -> 'Node':
    old_to_new = {}
    def dfs(node):
        if not node:
            return None
        if node in old_to_new:
            return old_to_new[node]
        clone = Node(node.val)
        old_to_new[node] = clone
        for neighbor in node.neighbors:
            clone.neighbors.append(dfs(neighbor))
        return clone
    return dfs(node)

def build_graph(adjList):
    if not adjList:
        return None
    nodes = [Node(i+1) for i in range(len(adjList))]
    for i, neighbors in enumerate(adjList):
        nodes[i].neighbors = [nodes[j-1] for j in neighbors]
    return nodes

def serialize_graph(node):
    if not node:
        return []
    from collections import deque
    visited = set()
    result = []
    queue = deque([node])
    val_to_index = {}
    nodes = []
    # Assign indices based on value-1, mapping val to index
    while queue:
        curr = queue.popleft()
        if curr.val not in visited:
            visited.add(curr.val)
            nodes.append(curr)
            for neighbor in curr.neighbors:
                queue.append(neighbor)
    nodes.sort(key=lambda x: x.val)
    for node in nodes:
        result.append([neighbor.val for neighbor in node.neighbors])
    return result


# Example 1
adj1 = [[2,4],[1,3],[2,4],[1,3]]
g1 = build_graph(adj1)
cg1 = cloneGraph(g1)
print(serialize_graph(cg1))  # Output: [[2, 4], [1, 3], [2, 4], [1, 3]]

# Example 2
adj2 = [[]]
g2 = build_graph(adj2)
cg2 = cloneGraph(g2)
print(serialize_graph(cg2))  # Output: [[]]

# Example 3
adj3 = []
g3 = build_graph(adj3)
cg3 = cloneGraph(g3)
print(serialize_graph(cg3))  # Output: []



"""
133. Clone Graph
Medium
Topics
premium lock iconCompanies

Given a reference of a node in a connected undirected graph.

Return a deep copy (clone) of the graph.

Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors.

class Node {
    public int val;
    public List<Node> neighbors;
}



Test case format:

For simplicity, each node's value is the same as the node's index (1-indexed). For example, the first node with val == 1, the second node with val == 2, and so on. The graph is represented in the test case using an adjacency list.

An adjacency list is a collection of unordered lists used to represent a finite graph. Each list describes the set of neighbors of a node in the graph.

The given node will always be the first node with val = 1. You must return the copy of the given node as a reference to the cloned graph.



Example 1:

Input: adjList = [[2,4],[1,3],[2,4],[1,3]]
Output: [[2,4],[1,3],[2,4],[1,3]]
Explanation: There are 4 nodes in the graph.
1st node (val = 1)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
2nd node (val = 2)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).
3rd node (val = 3)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
4th node (val = 4)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).

Example 2:

Input: adjList = [[]]
Output: [[]]
Explanation: Note that the input contains one empty list. The graph consists of only one node with val = 1 and it does not have any neighbors.

Example 3:

Input: adjList = []
Output: []
Explanation: This an empty graph, it does not have any nodes.



Constraints:

    The number of nodes in the graph is in the range [0, 100].
    1 <= Node.val <= 100
    Node.val is unique for each node.
    There are no repeated edges and no self-loops in the graph.
    The Graph is connected and all nodes can be visited starting from the given node.


"""

"""
Here’s a **Python DFS solution** for Leetcode 133 Clone Graph, with test helpers to build and serialize adjacency lists.

***

### Node Definition

```python
class Node:
    def __init__(self, val: int = 0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
```

***

### DFS Graph Cloning

```python
def cloneGraph(node: 'Node') -> 'Node':
    old_to_new = {}
    def dfs(node):
        if not node:
            return None
        if node in old_to_new:
            return old_to_new[node]
        clone = Node(node.val)
        old_to_new[node] = clone
        for neighbor in node.neighbors:
            clone.neighbors.append(dfs(neighbor))
        return clone
    return dfs(node)
```
- Stores cloned nodes in a hash map to avoid duplicates/cycles.[1][2]

***

### Helper: Build Graph from Adjacency List

```python
def build_graph(adjList):
    if not adjList:
        return None
    nodes = [Node(i+1) for i in range(len(adjList))]
    for i, neighbors in enumerate(adjList):
        nodes[i].neighbors = [nodes[j-1] for j in neighbors]
    return nodes
```

***

### Helper: Serialize Graph to Adjacency List

```python
def serialize_graph(node):
    if not node:
        return []
    from collections import deque
    visited = set()
    result = []
    queue = deque([node])
    val_to_index = {}
    nodes = []
    # Assign indices based on value-1, mapping val to index
    while queue:
        curr = queue.popleft()
        if curr.val not in visited:
            visited.add(curr.val)
            nodes.append(curr)
            for neighbor in curr.neighbors:
                queue.append(neighbor)
    nodes.sort(key=lambda x: x.val)
    for node in nodes:
        result.append([neighbor.val for neighbor in node.neighbors])
    return result
```

***

### Test Cases

```python
# Example 1
adj1 = [[2,4],[1,3],[2,4],[1,3]]
g1 = build_graph(adj1)
cg1 = cloneGraph(g1)
print(serialize_graph(cg1))  # Output: [[2, 4], [1, 3], [2, 4], [1, 3]]

# Example 2
adj2 = [[]]
g2 = build_graph(adj2)
cg2 = cloneGraph(g2)
print(serialize_graph(cg2))  # Output: [[]]

# Example 3
adj3 = []
g3 = build_graph(adj3)
cg3 = cloneGraph(g3)
print(serialize_graph(cg3))  # Output: []
```
***

This covers both the **DFS cloning** and end-to-end **adjacency list testing** for Leetcode 133.[2][1]

[1](https://algo.monster/liteproblems/133)
[2](https://neetcode.io/problems/clone-graph)
[3](https://www.geeksforgeeks.org/dsa/print-adjacency-list-of-a-bidirectional-graph/)
[4](https://blog.stackademic.com/clone-graph-9bde67e03d70)
[5](https://www.youtube.com/watch?v=2Qzj0t8nrCk)
[6](https://www.geeksforgeeks.org/dsa/clone-an-undirected-graph/)
[7](https://www.youtube.com/watch?v=vXkT2nYSde0)
[8](https://github.com/LeetCode-Feedback/LeetCode-Feedback/issues/26471)
[9](https://stackoverflow.com/questions/74438226/creating-an-adjacency-list-class-in-python)
[10](https://leetcode.com/discuss/interview-question/5039797/BFS-and-DFS-Graph-Problems:-Easy-to-Medium-Difficulty/)
[11](https://stackoverflow.com/questions/77903836/leetcode-133-clone-graph-dfs-deep-copy-is-not-getting-accepted)
[12](https://www.youtube.com/watch?v=S46c4KkLwPM)
[13](https://www.reddit.com/r/leetcode/comments/12d8cdc/i_have_accepted_the_fact_that_graph_problems_dfs/)
[14](https://leetcode.com/problems/clone-graph/)
[15](https://www.reddit.com/r/Python/comments/64vm47/best_way_to_represent_graph_data_structure_in/)
[16](https://algomap.io/problems/clone-graph)
[17](https://www.youtube.com/watch?v=mQeF6bN8hMk)
[18](https://www.finalroundai.com/articles/clone-a-graph)
[19](https://www.reddit.com/r/leetcode/comments/12fofd1/clone_graph_leetcode_133_python/)
[20](https://www.youtube.com/watch?v=wWE7YzuBBkE)
"""